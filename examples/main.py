import importlib

import pytest

if __name__ == "__main__":
    foobar = importlib.import_module("wiener.plugins.foobar")
    metadata = importlib.import_module("wiener.plugins.metadata")
    plugins = [getattr(m, "Plugin")() for m in [foobar, metadata]]
    pytest.main(["tests"], plugins=plugins)
