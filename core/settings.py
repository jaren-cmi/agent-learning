"""Day 1: 配置管理。用 pydantic-settings 从 .env 读取配置。"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    openai_api_key: str = ""
    openai_base_url: str = "https://api.openai.com/v1"
    default_model: str = "gpt-4o-mini"

    tavily_api_key: str = ""

    log_level: str = "INFO"
    log_json: bool = False

    # Agent 熔断上限：防止死循环烧钱
    max_steps: int = Field(default=10, ge=1, le=50)
    max_cost_usd: float = Field(default=0.5, gt=0)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


if __name__ == "__main__":
    print(settings.model_dump(exclude={"openai_api_key", "tavily_api_key"}))
