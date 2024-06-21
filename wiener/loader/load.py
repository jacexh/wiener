import importlib


def load(*args: str):
    plugins = []
    for arg in args:
        module = importlib.import_module("wiener.plugins.{}".format(arg))
        plugins.append(getattr(module, "Plugin")())
    return plugins
