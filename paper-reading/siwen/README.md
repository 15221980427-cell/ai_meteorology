# Siwen · 气象 AI 文献阅读库

本目录用于**气象 AI、全球天气预报、风功率预测、物理引导风场预测**的系统阅读和组会交流，兼顾新入门的硕士生与后续项目研究。

> **推荐阅读顺序：** 先看 01 综述建立知识地图 → 再按兴趣阅读 02 全球天气预报 / 03 风功率预测 → 最后通过组会讨论学习研究方法和实验验证。阅读笔记是二次整理，具体结论应以原论文为准。

## 目录导航

| 主题 | 适合谁 | 主要内容 |
|---|---|---|
| [01 · 气象 AI 综述](01-气象AI综述/) | 两名硕士生共同入门 | 气象数值预报、深度学习、基础模型的发展与局限 |
| [02 · 全球天气预报模型](02-全球天气预报模型/) | 全球预测方向 | ClimaX、GraphCast、GenCast：预训练、确定性预报、概率预报 |
| [03 · 风功率预测](03-风功率预测/) | 风电预测方向 | 深度表征方法、时序模型、多源数据、评价指标 |
| [组会讨论](组会讨论/) | 全组 | 风场预测、PINN、PD-WPN、SCADA、实验有效性 |
| [paper/](paper/) | PDF 原文管理 | 已有来源链接和待补全 PDF 清单 |
| [images/](images/) | 配图资源 | 文献笔记配图，保持相对链接 |

## 四周入门计划

1. **第 1 周 · 了解气象和 AI：** 阅读 [气象与数值天气预报综述](01-气象AI综述/artificial-intelligence-numerical-weather-prediction-survey.md) 和 [基础模型综述](01-气象AI综述/deep-learning-foundation-models-weather-prediction-survey.md)。交付一张模型演进路线图。
2. **第 2 周 · 学会对比模型：** 阅读 [GraphCast](02-全球天气预报模型/learning-skillful-medium-range-global-weather-forecasting.md)、[GenCast](02-全球天气预报模型/probabilistic-weather-forecasting-with-machine-learning-gencast.md)、[ClimaX](02-全球天气预报模型/climax-foundation-model-for-weather-and-climate.md) 的结构与测试方法。关注预报时间、空间分辨率和概率预测。
3. **第 3 周 · 联系应用：** 阅读 [风功率预测综述](03-风功率预测/wind-power-forecasting-deep-representation-survey.md)，再看 [组会讨论的应用论文](组会讨论/README.md)。关注观测数据、预测目标和基线模型。
4. **第 4 周 · 输出可验证的研究问题：** 两人分别提出风功率预测、垂直风切变/雷达预测的最小可行实验，写明数据划分、对照实验、评价指标和不足。

## 每篇阅读笔记至少回答

1. **问题：** 论文解决什么问题？属于天气预报、风场预测还是风功率预测？
2. **数据：** 数据来源是什么？时间与空间分辨率？训练、验证、测试如何划分？
3. **方法：** 输入、网络结构、损失函数、物理信息和输出是什么？
4. **实验：** 与什么基线相比？有哪些消融实验？性能提升是否可比较？
5. **局限：** 如果用于我们的雷达多高度风场 / 风切变预警或风电预测，什么结论不能直接迁移？

## 贡献方式

- 新增阅读笔记时，请优先放入相应主题目录，文件名使用小写英文和连字符（例如 `wind-profile-forecasting.md`）。
- 图片统一放在 `images/`，主题子目录的 Markdown 用 `../images/filename.png` 引用；组会讨论保留其原有 `assets/` 目录。
- 在笔记开头注明论文题目、作者、发表年份、DOI/原文链接、数据和代码地址（如有）。
- 提交内容通过独立分支 + Pull Request，由负责人检查后合并。
- **不要提交敏感雷达观测数据、密钥或未获授权公开的论文全文。**

## 原始来源

部分笔记由 [SHU CrossDomain AI Lab / research-hub](https://github.com/Shu-CrossDomain-AI-Lab/research-hub/tree/main/paper-reading/siwen-chen) 迁移整理。原文献笔记的正文内容予以保留，主要调整了分类路径、导航和配图链接。
