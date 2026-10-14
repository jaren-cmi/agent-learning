# agent-learning

系统性学习 **Agent 开发** 的实践仓库（Python）。

## 学习路线

| 阶段 | 天数 | 主题 | 产出项目 |
|---|---|---|---|
| 阶段 0 | Day 1–10 | 工程打底：asyncio / pydantic / 流式 / 测试 / Docker | `core/` 脚手架 |
| 阶段 1 | Day 11–25 | 手写 LLM 原语与 Agent 主循环（**不用框架**） | 项目①：ReAct Agent |
| 阶段 2 | Day 26–40 | RAG 与记忆系统 | 项目②：知识库问答 Agent |
| 阶段 3 | Day 41–60 | LangGraph / MCP / 多 Agent 编排 | 项目③：自动调研报告生成器 |
| 阶段 4 | Day 61–80 | 生产化：可观测、评测、安全、部署 | 上线与开源 |

> ⚠️ **Day 16 / Day 18 是生死线**：没完全吃透 tool-calling 循环，后面全是黑箱，宁可多花几天。

## 目录结构

```
core/        # 逐步沉淀的可复用基建（http / schema / logging / tools / agent ...）
days/        # 每日练习，一天一个目录 d01, d02, ...
tests/       # pytest 测试
prompts/     # prompt 版本管理
evals/       # 评测集与评测脚本
docs/        # 学习笔记与设计文档
```

## 快速开始

```bash
pip install uv
uv sync --extra dev
cp .env.example .env   # 填入你的 API key
uv run pytest
```

## 每日工作法

1. 打开当天的 issue，照着「任务 / 产出物」做。
2. 代码放 `days/dXX/`，可复用部分重构进 `core/`。
3. 当天结束 commit 一次，并在 issue 里写 3 行收获后关闭。
4. 每周末留半天复盘重构。

**没有产出物就不算完成。**
