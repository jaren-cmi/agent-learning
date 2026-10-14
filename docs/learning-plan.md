# Agent 开发 80 天任务清单

> 每天 1.5~3 小时。每日任务都有「产出物」——没有产出物就不算完成。

## 阶段 0：工程打底（Day 1–10）

| Day | 主题 | 产出物 |
|---|---|---|
| 1 | 环境与项目骨架（uv / pydantic-settings / .gitignore） | 可运行的空项目 + `core/settings.py` |
| 2 | asyncio 基础：协程、事件循环、gather | `days/d02/async_basics.py` 串行 vs 并行耗时对比 |
| 3 | 异步进阶：Semaphore 限流、wait_for 超时、异常处理 | `days/d03/concurrent_fetch.py` |
| 4 | httpx 与 SSE 流式、tenacity 重试 | `core/http.py` 的 `stream_sse()` |
| 5 | pydantic v2 核心：校验器、JSON Schema | `days/d05/models.py` |
| 6 | 类型注解 → 自动生成 tool schema | `core/schema.py` 的 `func_to_schema()` |
| 7 | FastAPI + SSE 服务端 | `days/d07/server.py` |
| 8 | pytest / pytest-asyncio / mock | `tests/` 全绿 |
| 9 | 结构化日志 + Docker | `docker compose up` 可跑 |
| 10 | 整合复盘，零件收进 `core/` | 更新 README + 笔记 |

**阶段自检**：能否 10 分钟内从零搭出「异步 + 限流 + 重试 + 流式 + 校验」的脚手架？

## 阶段 1：手写 Agent 原语（Day 11–25）⭐最关键

> **本阶段禁止使用任何 Agent 框架。**

| Day | 主题 | 产出物 |
|---|---|---|
| 11 | 裸 HTTP 调 Chat API | `days/d11/raw_call.py` |
| 12 | 消息结构与「模型无状态」本质 | `days/d12/conversation.py` + 笔记 |
| 13 | 流式输出打字机效果 | `days/d13/stream_chat.py` |
| 14 | tiktoken 计费与上下文窗口 | `days/d14/token_counter.py` + 价格对照表 |
| 15 | 结构化输出（JSON Schema） | `days/d15/structured.py` |
| 16 | **Tool Calling 单轮全手写** | `days/d16/tool_single.py` ⭐分水岭 |
| 17 | 工具注册表（装饰器 + 校验 + 异常捕获） | `core/tools.py` |
| 18 | **Agent 主循环 + 三道熔断** | `core/agent.py` ⭐项目①雏形 |
| 19 | 三个真工具：计算器 / 搜索 / 文件 | `tools/` + 单测 |
| 20 | ReAct 与 Prompt 工程对比实验 | `prompts/` 3 个版本 + 对比笔记 |
| 21 | Trace 与调试可视化 | `core/trace.py` |
| 22 | 错误处理与鲁棒性（4 类故障） | `tests/test_agent_robust.py` |
| 23 | 上下文管理：滑窗 + 摘要压缩 | `core/context.py` |
| 24 | 推理模型与模型路由抽象 | `core/llm.py` |
| 25 | 项目① 验收（CLI + README） | 可用的 ReAct Agent |

**阶段自检**：不看代码能口述完整 tool-calling 循环；工具报错时 Agent 自我修正；有步数/成本熔断。

## 阶段 2：RAG 与记忆（Day 26–40）

| Day | 主题 | 产出物 |
|---|---|---|
| 26 | Embedding 与余弦相似度 | `days/d26/embedding_play.py` |
| 27 | 最小 RAG（numpy 暴力检索，不用向量库） | `days/d27/mini_rag.py` |
| 28 | 向量数据库 Chroma / HNSW 原理 | `core/vectorstore.py` |
| 29 | 文档加载：PDF / MD / HTML + 元数据 | `rag/loaders.py` |
| 30 | 分块策略三种对比 | `rag/chunking.py` + 对比表 |
| 31 | 混合检索 BM25 + 向量 + RRF | `rag/hybrid.py` |
| 32 | Rerank 重排序 | `rag/rerank.py` |
| 33 | 查询改写 / 多查询 / HyDE | `rag/query_transform.py` |
| 34 | 引用与防幻觉校验 | `rag/cite.py` |
| 35 | **RAG 评测基线（Recall@k / Ragas）** | `evals/rag_eval.py` ⭐基线分数务必保留 |
| 36 | Agentic RAG：检索变成工具 | 对比结论 |
| 37 | 短期记忆：滑窗 + 滚动摘要 | `memory/short_term.py` |
| 38 | 长期记忆：事实抽取 + 去重冲突 | `memory/long_term.py` |
| 39 | 持久化：会话 / 消息 / trace | `storage/` |
| 40 | 项目② 验收 | 带引用的知识库问答 Agent |

## 阶段 3：框架与多 Agent（Day 41–60）

| Day | 主题 | 产出物 |
|---|---|---|
| 41 | LangGraph 入门，重写 Day 18 循环 | 对比笔记 |
| 42 | State / Reducer / Checkpoint 断点续跑 | 可恢复的 Agent |
| 43 | Human-in-the-loop 中断审批 | `days/d43/hitl.py` |
| 44 | 条件路由与子图 | 架构 mermaid 图 |
| 45 | Reflection 自我批评循环 | `patterns/reflection.py` |
| 46 | Planner–Executor | `patterns/plan_execute.py` |
| 47 | Supervisor 多 Agent handoff | `patterns/supervisor.py` |
| 48 | 并行 fan-out / Map-Reduce | `patterns/parallel.py` |
| 49 | MCP ���念 + 接入现成 Server | `days/d49/mcp_client.py` |
| 50 | **手写 MCP Server（FastMCP）** | `mcp_server/` 在编辑器中可用 |
| 51 | 框架横向对比（Agents SDK / Pydantic AI） | `docs/comparison.md` |
| 52 | 项目③ 设计（先设计再写码） | `docs/DESIGN.md` |
| 53 | Planner 节点：拆 5~8 个子问题 | 节点实现 |
| 54 | 并行 Research 节点 | 节点实现 |
| 55 | Writer 节点（强制引用） | 节点实现 |
| 56 | Critic 节点（打分 + 返工，限 3 轮） | 节点实现 |
| 57 | 人工审批 + 导出 + checkpoint 恢复 | 端到端可跑 |
| 58 | astream_events 流式推进度到前端 | 实时 UI |
| 59 | 压测 10 个主题，修 3 类失败 | `docs/report.md` |
| 60 | 阶段 3 验收 | 状态图 + 成本上限 |

## 阶段 4：生产化（Day 61–80）

| Day | 主题 | 产出物 |
|---|---|---|
| 61 | 接入 Langfuse / LangSmith | 可回放 trace |
| 62 | OpenTelemetry 全链路埋点 | `core/otel.py` |
| 63 | 评测集建设（50 条分层用例） | `evals/dataset.jsonl` |
| 64 | 自动评测与指标 | `uv run eval` 出报告 |
| 65 | LLM-as-a-Judge + 人工校准 | 一致性数据 |
| 66 | CI 回归，分数下降即失败 | `.github/workflows/eval.yml` |
| 67 | **Prompt Injection 攻防（10 条用例）** | `security/injection_tests.py` |
| 68 | 代码沙箱执行（Docker 隔离） | `tools/sandbox.py` |
| 69 | 输入输出 Guardrails / PII 脱敏 | `security/guardrails.py` |
| 70 | 权限、密钥管理、审计日志 | `security/authz.py` |
| 71 | 限流、配额、熔断降级 | `core/resilience.py` |
| 72 | 精确缓存 / 语义缓存 / Prompt Caching | 成本下降数据 |
| 73 | 异步任务队列（arq / Celery） | `worker.py` |
| 74 | API 完善：鉴权 / 幂等 / 优雅关闭 | `api/` |
| 75 | Docker Compose 全栈部署 | 一条命令起服务 |
| 76 | 性能优化：并行化 / 模型路由 | 前后对比表 |
| 77 | 本地模型 Ollama / vLLM / 量化 | 实验报告 |
| 78 | 监控告警看板 | Dashboard |
| 79 | 读源码：Aider / OpenHands | `docs/source_notes.md` |
| 80 | 总验收：上线 + 博客 + 开源 | 最终清单全绿 |

## 推荐资料

- Anthropic《Building Effective Agents》（建议读 3 遍）
- OpenAI《A Practical Guide to Building Agents》
- LangGraph 官方 Academy
- MCP 官方文档 modelcontextprotocol.io
- 开源精读：OpenHands、Aider、Dify

## 四条避坑忠告

1. 别急着上框架 —— 没手写过 tool-calling 循环就用框架，出问题无法 debug。
2. 能用固定工作流解决的，别用 Agent —— 先问「这一步真的需要模型决策吗？」
3. 评测要和���码同步建 —— 没有评测集，每次改 prompt 都是赌博。
4. 上下文工程 > prompt 工程 —— 差距在「喂什么信息、怎么组织、怎么压缩」。
