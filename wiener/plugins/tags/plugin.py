import pytest


class Plugin:
    def pytest_configure(self, config: pytest.Config):
        config.addinivalue_line("markers", "smoke: 冒烟测试用例")
        config.addinivalue_line("markers", "regression: 冒烟测试用例")
