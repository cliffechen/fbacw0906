# Amazon Supplement Copywriting

面向亚马逊美国站膳食补充剂的便携 AI 写作技能。根据产品事实、买家问题和使用场景，产出自然克制、具体且略有温度的美式英文文案，配合中文解释与设计建议。

本项目是技能文本、参考指南与交付模板，不是独立运行的应用。核心写作流程不要求联网、关键词库或额外工具。

## 能写什么

- **副图文案**：每张图围绕一个买家问题，交付英文主标题、支撑句、必要事实标签、视觉建议、依据与限定说明，以及一个不同角度的备选标题。
- **A+ 图片文案**：按内容类型组合模块；未指定时使用 Basic，Brand Story 单独处理。
- **商品标题与五点描述**：自然使用相关关键词，也支持包含上述内容的完整文案包。
- **局部改写**：只请求副图就只交付副图，不自动扩展范围。

默认英文成稿、中文说明。保留 AG1、Ritual/HUM、Onnit、Thorne 风格参考，可调节语气与信息密度；品牌参考不代表可以借用其商标、口号、研究或认证。

## 快速开始

1. 保留整个 `amazon-supplement-copywriting/` 文件夹及其相对路径。
2. 让能够读取本地文件的 AI 助手先阅读 [SKILL.md](amazon-supplement-copywriting/SKILL.md)，再按其中的指引读取相关参考文件。
3. 提供产品资料和交付需求。优先提供标签、剂量、包装数量、使用方法及对应来源；竞品图片、评论和关键词库均为可选资料。

可复制下面的请求，并把示例资料替换为本品已确认的信息：

```text
请先阅读 amazon-supplement-copywriting/SKILL.md，按该技能写作。

交付范围：只写 3 张副图。
风格：清晰、克制、略有温度。
产品资料：附上本品标签、包装图和使用说明，并标明资料来源。
目标买家与场景：填写已知信息；没有调研时请标注为买家假设。
竞品资料与关键词库：本次不提供。

每张图提供推荐标题和一个不同角度的备选，附中文推荐理由。
缺少依据的功效、认证或使用体验不要补写。
```

需要完整包时，把交付范围改为“商品标题、五点、副图和 Basic A+”，并补充所需副图数量。已有品牌语气或 A+ 类型要求时，直接写入请求。

## 输出如何交给设计师

按照 [交付模板](amazon-supplement-copywriting/assets/copy-package-template.md)，消费者看到的英文正文与内部中文说明分开列出。视觉建议说明主体、场景、文字层级和建议断行；必须上图的限定说明会单独标明。

图片主标题通常为 3–7 词，支撑句通常为 8–16 词。这是可调整的编辑预算，不是平台硬性限制。主图、商品标题、副图标题和 A+ 标题在流程中分别处理。

## 项目结构

| 路径 | 用途 |
|---|---|
| [SKILL.md](amazon-supplement-copywriting/SKILL.md) | 写作入口与完整流程 |
| [美式图片文案编辑指南](amazon-supplement-copywriting/references/american-image-copy.md) | 英文编辑、具体性与自然表达检查 |
| `amazon-supplement-copywriting/references/` | 品牌语气、写作结构、版式、声明核对及历史案例 |
| `amazon-supplement-copywriting/assets/` | 可分层排版的交付模板 |
| `amazon-supplement-copywriting/research/` | 可选原始研究素材，日常写作无需全部加载 |
| `amazon-supplement-copywriting/evals/` | 验证场景、新旧输出与评审记录 |
| `tests/` | 仓库约定、技能入口和文档链接检查 |
| [AGENTS.md](AGENTS.md) | 项目修改、测试与提交约定 |

## 事实与表达边界

竞品广告只用于学习沟通方式，评论只用于理解顾虑与用语，二者都不能证明本品功效。缺少依据时，不能通过改成 “supports”、添加“调研显示”或免责声明保留原承诺。标签用量、每份含量和包装数量必须保持一致。

具体核对方法见 [事实与声明指南](amazon-supplement-copywriting/references/compliance-fda-ftc.md)。平台字段与版式参考见 [亚马逊版式指南](amazon-supplement-copywriting/references/amazon-layout.md)，其中记录了规则来源及核验日期。生成内容仍需品牌结合实际产品资料审阅。

## 验证与维护

维护测试使用 Python 标准库，无需安装第三方测试依赖。在仓库根目录运行：

```bash
python -B -X utf8 -m unittest discover -s tests -v
git diff --check
```

自动化测试检查文件结构和文档引用，不评价英文吸引力。文案验证另覆盖独立份装粉剂、瓶装粉剂、胶囊、仅产品资料、竞品评论、无依据功效或认证六类输入，保留新旧输出、独立评审及定向复验记录。

详见 [验证场景](amazon-supplement-copywriting/evals/scenarios.md) 与 [验证报告](amazon-supplement-copywriting/evals/validation-report.md)。案例均为虚构；AI 评审不等于美国消费者验证，也不证明购买转化提升。

每次修改需按 [AGENTS.md](AGENTS.md) 更新相关测试，确保测试与验证通过，并创建对应 Git commit。
