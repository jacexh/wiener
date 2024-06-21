import pytest

from wiener.loader import load

if __name__ == "__main__":
    pytest.main(["tests"], plugins=load("foobar", "tags"))
