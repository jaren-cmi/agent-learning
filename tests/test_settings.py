"""Day 1 冒烟测试：配置能正常加载。"""

from core.settings import Settings


def test_settings_defaults():
    s = Settings(_env_file=None)
    assert s.default_model
    assert s.max_steps >= 1
    assert s.max_cost_usd > 0
