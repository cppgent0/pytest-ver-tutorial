import unittest

import pytest
from pytest_ver import pth


# -------------------
class TestPoc(unittest.TestCase):

    # -------------------
    def setUp(self):
        pass

    # --------------------
    def tearDown(self):
        pth.report()

    # --------------------
    def test_init1(self):
        # declare a new protcol id and it's description
        pth.proto.protocol('tp-001', 'test the init function')

        # declare some setup steps
        pth.proto.step('setup some stuff1')
        x = 1
        pth.proto.step('setup more stuff2')
        y = x
        self.assertEqual(x, y)

        pth.proto.step('verify1 everything is equal')
        # do a verification against a requirement
        pth.ver.verify(x == y, reqid='SRS-001')
        pth.ver.verify(x == 1, reqid='SRS-001')
        # since all verifys passed, this step's result is PASS

        pth.proto.step('verify2')
        pth.ver.verify(False, reqid='SRS-002')
        pth.ver.verify(True, reqid='SRS-002')
        pth.ver.verify(True, reqid='SRS-002')
        # since one verify failed, this step's result is FAIL

        pth.proto.step('verify3')
        pth.ver.verify(True, reqid='SRS-003')
        pth.ver.verify(True, reqid='SRS-003')
        pth.ver.verify(False, reqid='SRS-003')
        # since one verify failed, this step's result is FAIL

    # --------------------
    @pytest.mark.smoketest1
    def test_init2(self):
        pth.proto.protocol('tp-002', 'test the init2')

        pth.proto.step('verify1 everything is equal')
        pth.ver.verify(1 == 1, reqid='SRS-001')
        # note: this is the second time this requirment is verified

    # --------------------
    def test_init3(self):
        pth.proto.protocol('tp-003', 'test the init3')

        pth.proto.step('verify1 everything is equal')
        pth.ver.verify(1 == 1, reqid='SRS-004')
