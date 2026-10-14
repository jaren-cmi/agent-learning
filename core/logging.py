"""Day 9: 结构化日志。

TODO(Day 9): 接入 structlog，支持 JSON 输出，并把 trace_id 注入上下文。
"""

import logging
import sys

from core.settings import settings


def setup_logging() -> None:
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)-8s %(name)s | %(message)s",
        stream=sys.stdout,
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
