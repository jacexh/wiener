# -*- coding: utf-8 -*-

import unittest

from wiener.plugins.metadata import metadata


class TestExample(unittest.TestCase):
    def test_001(self):
        pass

    @metadata.smoke
    def test_002(self):
        pass

    def test_003(self):
        pass
