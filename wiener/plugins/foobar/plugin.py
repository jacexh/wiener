# -*- coding: utf-8 -*-
import random
import time

import pytest


class Plugin:
    def pytest_runtest_protocol(self, item: pytest.Item):
        # if item.nodeid.endswith("test_002"):
        #     item.session.shouldstop = True
        sec = random.randint(1, 2)
        print("execute {} after {} second(s)".format(item.nodeid, sec))
        time.sleep(sec)
