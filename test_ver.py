import unittest

import pytest

from pytest_ver import pth


# -------------------
class TestPoc(unittest.TestCase):

    # --------------------
    @classmethod
    def setUpClass(cls):
        pth.init()

    # -------------------
    def setUp(self):
        pass

    # -------------------
    def tearDown(self):
        pass

    # --------------------
    @classmethod
    def tearDownClass(cls):
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
        pth.ver.verify_equal(x, y, reqids='SRS-001')
        pth.ver.verify_equal(x, 1, reqids='SRS-001')
        # since all verifys passed, this step's result is PASS

        pth.proto.step('verify2')
        pth.ver.verify(False, reqids='SRS-002')
        pth.ver.verify(True, reqids='SRS-002')
        pth.ver.verify(True, reqids='SRS-002')
        # since one verify failed, this step's result is FAIL

        pth.proto.step('verify3')
        pth.ver.verify(True, reqids='SRS-003')
        pth.ver.verify(True, reqids='SRS-003')
        pth.ver.verify(False, reqids='SRS-003')
        # since one verify failed, this step's result is FAIL

    # --------------------
    @pytest.mark.smoketest1
    def test_init2(self):
        pth.proto.protocol('tp-002', 'test the init2')

        pth.proto.step('verify1 everything is equal')
        pth.ver.verify_equal(1, 1, reqids='SRS-001')
        # note: this is the second time this requirment is verified

    # --------------------
    def test_init3(self):
        pth.proto.protocol('tp-003', 'test the init3')

        pth.proto.step('verify1 everything is equal')
        pth.ver.verify_equal(1, 1, reqids='SRS-004')
