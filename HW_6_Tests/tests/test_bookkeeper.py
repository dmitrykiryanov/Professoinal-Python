from HW_6_Tests.bookkeeper import get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, add_new_doc, delete_doc
import unittest

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

class TestFunctions(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('10006'), "Аристарх Павлов")

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('11-2'), "Геннадий Покемонов")

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(),{'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'})

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf("2207 876234"), '1')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('1111111', 'passport', 'Иванов Иван', '3'), '3')

    def test_delete_doc(self):
        delete_doc('1111111')
        self.assertNotIn('1111111', documents)
        self.assertNotIn('1111111', directories)

    def tearDown(self):
        print('method tearDown')