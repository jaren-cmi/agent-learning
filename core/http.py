"""Day 3-4: 带重试、限流、超时的异步 HTTP 客户端。

TODO(Day 4): 用 tenacity 加指数退避重试
TODO(Day 4): 实现 stream_sse()，逐块 yield SSE 事件
"""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

import httpx


class AsyncHTTP:
    """复用连接池 + 信号量限流的异步客户端。"""

    def __init__(self, *, concurrency: int = 5, timeout: float = 30.0) -> None:
        self._sem = asyncio.Semaphore(concurrency)
        self._client = httpx.AsyncClient(timeout=timeout)

    async def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        async with self._sem:
            resp = await self._client.request(method, url, **kwargs)
            resp.raise_for_status()
            return resp

    async def get_json(self, url: str, **kwargs: Any) -> Any:
        return (await self.request("GET", url, **kwargs)).json()

    async def stream_sse(self, url: str, **kwargs: Any) -> AsyncIterator[str]:
        """TODO(Day 4): 解析 `data: ` 前缀，遇到 [DONE] 结束。"""
        raise NotImplementedError("Day 4 任务")

    async def aclose(self) -> None:
        await self._client.aclose()


@asynccontextmanager
async def http_client(**kwargs: Any) -> AsyncIterator[AsyncHTTP]:
    client = AsyncHTTP(**kwargs)
    try:
        yield client
    finally:
        await client.aclose()
