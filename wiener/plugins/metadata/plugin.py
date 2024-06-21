import pytest


class Plugin:
    def pytest_configure(self, config: pytest.Config):
        config.addinivalue_line("markers", "smoke: mark test to run only on named environment")
