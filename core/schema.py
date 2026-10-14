"""Day 6: 把带类型注解的 Python 函数自动转成 LLM tool schema。

这是整个 Agent 的核心基建 —— **务必自己写出来，不要抄**。

目标：
    def get_weather(city: str, unit: Literal["c", "f"] = "c") -> str:
        '''查询城市天气。'''

    func_to_schema(get_weather) ==
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "查询城市天气。",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {"type": "string"},
            "unit": {"type": "string", "enum": ["c", "f"], "default": "c"}
          },
          "required": ["city"]
        }
      }
    }

提示：
- inspect.signature() 拿参数与默认值
- typing.get_type_hints() 拿类型
- 也可以用 pydantic.create_model() + model_json_schema() 偷懒，但先手写一遍
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


def func_to_schema(fn: Callable[..., Any]) -> dict[str, Any]:
    """TODO(Day 6): 实现我。"""
    raise NotImplementedError("Day 6 任务")
