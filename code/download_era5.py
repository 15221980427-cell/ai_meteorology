#!/usr/bin/env python3
"""按月下载长三角 ERA5 小时单层数据；默认仅生成请求计划。"""

import argparse
import calendar
import datetime as dt
import json
import os
from pathlib import Path


DATASET = "reanalysis-era5-single-levels"
# 北、西、南、东：覆盖沪苏浙皖的矩形，包含邻近地区及近海。
DEFAULT_AREA = [35.5, 114.5, 27.0, 123.0]
GROUPS = {
    "wind_temperature": [
        "10m_u_component_of_wind", "10m_v_component_of_wind",
        "100m_u_component_of_wind", "100m_v_component_of_wind",
        "2m_temperature", "2m_dewpoint_temperature",
    ],
    "pressure_cloud": [
        "surface_pressure", "mean_sea_level_pressure", "total_cloud_cover",
        "low_cloud_cover", "boundary_layer_height", "total_column_water_vapour",
    ],
    "precipitation_radiation": [
        "total_precipitation", "surface_solar_radiation_downwards",
        "surface_thermal_radiation_downwards", "surface_net_solar_radiation",
    ],
}


def monthly_requests(start, end, area, groups):
    """生成包含首尾日期的逐月请求，每天 24 个 UTC 时次。"""
    month = start.replace(day=1)
    while month <= end:
        last = month.replace(day=calendar.monthrange(month.year, month.month)[1])
        first_day = max(start, month).day
        last_day = min(end, last).day
        for group in groups:
            request = {
                "product_type": ["reanalysis"],
                "variable": GROUPS[group],
                "year": [str(month.year)],
                "month": [f"{month.month:02d}"],
                "day": [f"{day:02d}" for day in range(first_day, last_day + 1)],
                "time": [f"{hour:02d}:00" for hour in range(24)],
                "area": area,
                "data_format": "netcdf",
                "download_format": "zip",
            }
            label = f"{month.year}{month.month:02d}_{first_day:02d}-{last_day:02d}_{group}"
            yield label, request
        month = (last + dt.timedelta(days=1)).replace(day=1)


def date_value(value):
    try:
        return dt.datetime.strptime(value, "%Y%m%d").date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("日期须为有效的 YYYYMMDD，例如 20260930") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=date_value, default=dt.date(2024, 1, 1))
    parser.add_argument("--end", type=date_value, default=dt.date(2026, 9, 30))
    parser.add_argument("--area", nargs=4, type=float, default=DEFAULT_AREA,
                        metavar=("NORTH", "WEST", "SOUTH", "EAST"))
    parser.add_argument("--groups", nargs="+", choices=list(GROUPS), default=list(GROUPS))
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "data" / "era5")
    parser.add_argument("--download", action="store_true", help="实际提交下载；默认只打印计划")
    args = parser.parse_args()
    if args.start > args.end:
        parser.error("开始日期不能晚于结束日期")
    north, west, south, east = args.area
    if not (-90 <= south < north <= 90 and -180 <= west < east <= 180):
        parser.error("区域须满足 -90 <= 南 < 北 <= 90，-180 <= 西 < 东 <= 180")
    if args.download and args.end > dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=5):
        parser.error("结束日期过近或在未来：ERA5T 通常滞后约 5 天，请缩短范围并检查 CDS 可用日期")
    jobs = list(monthly_requests(args.start, args.end, args.area, list(dict.fromkeys(args.groups))))
    print(f"数据集：{DATASET}；UTC 小时数据；区域 N/W/S/E：{args.area}")
    print(f"日期：{args.start} 至 {args.end}；共 {len(jobs)} 个请求；目录：{args.output}")
    if not args.download:
        for label, request in jobs:
            print(json.dumps({"label": label, "request": request}, ensure_ascii=False))
        return
    try:
        import cdsapi
    except ImportError:
        parser.error("请先运行 python -m pip install -r code/requirements-era5.txt")
    client = cdsapi.Client()
    args.output.mkdir(parents=True, exist_ok=True)
    for label, request in jobs:
        # 将完整请求纳入名称，避免更换区域后误用旧数据。
        import hashlib
        digest = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()[:16]
        target = args.output / f"era5_{label}_{digest}.zip"
        metadata = target.with_suffix(".request.json")
        if target.is_file() and target.stat().st_size > 0 and metadata.is_file():
            if json.loads(metadata.read_text()) == request:
                print(f"跳过已完成：{target.name}")
                continue
        partial = target.with_suffix(".zip.part")
        print(f"下载：{target.name}", flush=True)
        client.retrieve(DATASET, request).download(str(partial))
        # 避免把失败/截断下载记录为已完成。
        import zipfile
        with zipfile.ZipFile(partial) as archive:
            if not archive.namelist() or archive.testzip() is not None:
                raise RuntimeError(f"下载文件校验失败：{partial}")
        os.replace(partial, target)
        metadata.write_text(json.dumps(request, indent=2) + "\n")
        print(f"完成：{target.name}", flush=True)


if __name__ == "__main__":
    main()
