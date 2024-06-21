# -*- coding: utf-8 -*-

import unittest

from wiener.plugins.tags import testcase


class TestExample(unittest.TestCase):
    @testcase.regression
    def test_001(self):
        pass

    @testcase.smoke
    def test_002(self):
        pass

    def test_003(self):
        pass
