# ERA5 长江三角洲小时数据下载

默认时间为 **2024-01-01 至 2026-09-30，包含首尾日期**。9 月没有 31 日。
时次为 UTC 每天 00:00–23:00，北京时间需加 8 小时。默认区域为
北 35.5°、西 114.5°、南 27.0°、东 123.0°，是覆盖上海、江苏、浙江、安徽的矩形，
不是行政边界裁剪；包含邻近地区和近海。采用 CDS 的 ERA5 单层默认 0.25° 网格。

## 配置与运行

1. 在 <https://cds.climate.copernicus.eu/> 注册/登录，并在
   <https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels>
   接受数据使用条款。
2. 按 CDS 个人页面的 API 指引配置 `~/.cdsapirc`（不要提交到 Git），或通过运行环境
   安全提供 `CDSAPI_URL=https://cds.climate.copernicus.eu/api` 和 `CDSAPI_KEY`。
   不要在聊天或代码中填写个人密钥。
3. 在仓库根目录运行：

```bash
python -m pip install -r code/requirements-era5.txt
# 只查看请求计划，不需要密钥，也不会下载
python code/download_era5.py
# 首先下载一天，验证账户权限、格式和数据
python code/download_era5.py --start 20240101 --end 20240101 --download
# 下载整个时间范围（耗时和数据量较大）
python code/download_era5.py --download
# 自定义范围、变量组和输出目录
python code/download_era5.py --area 33 118 28 123 --groups wind_temperature --download
```

数据按月、按变量组顺序提交，保存到 `data/era5/`，格式为包含 NetCDF 的 ZIP。
保存请求元数据用于复现；已完成且请求一致的文件再次运行会跳过。
中断后重跑会重新下载未完成的那一组，不是按字节断点续传。
下载后校验 ZIP 内容，失败时停止并保留 `.part` 文件，不会标记为完成。
CDS 队列、账户授权、网络策略及数据发布状态可能影响下载。
ERA5T 通常滞后约 5 天，最近数月可能仍为初步数据，最终 ERA5 通常滞后约 2–3 个月；
2026 年 9 月数据应核对 CDS 实际可用日期和最终化状态。

## 变量与使用注意

| 变量组 | 内容 |
| --- | --- |
| wind_temperature | 10 米与 100 米 u/v 风分量、2 米温度、2 米露点 |
| pressure_cloud | 地表气压、海平面气压、总云量、低云量、边界层高度、整层水汽 |
| precipitation_radiation | 总降水、向下短波/长波辐射、净短波辐射 |

风速由 `sqrt(u**2 + v**2)` 计算，单位 m/s；同时保留 u/v 有助于预测风向。
温度单位 K，转摄氏度减 273.15；气压单位 Pa；降水单位 m。
辐射是累计能量 J/m²，处理为平均通量 W/m² 时须按产品定义的累计时段换算。
请检查 NetCDF 中的时间、单位、累计约定及 `expver`，不要将所有变量视为瞬时量。

这些是再分析数据，不是业务预报。在训练预测模型时按时间划分训练/验证/测试集，
避免将未来时刻的再分析变量作为实时可用输入。高空环流建模还需要另行下载
ERA5 pressure levels；风电功率预测还需要实测功率、场站位置及机组信息。
