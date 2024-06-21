import pytest


class _Testcase:
    smoke = pytest.mark.smoke()
    regression = pytest.mark.regression()


testcase = _Testcase()
