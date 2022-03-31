from HW_6_Tests.yandex_folder import YandexDisk, TOKEN
import unittest

yd = YandexDisk(token=TOKEN)
yd_2 = YandexDisk(token='false_token')
class TestYaDisk(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_response(self):
        self.assertEqual(yd.make_folder('new_name_1'), 201)
    def test_response_2 (self):
        self.assertEqual(yd.make_folder('new_name_1'), 409)
    def test_false_token(self):
        self.assertEqual(yd_2.make_folder('false_folder'), 401)