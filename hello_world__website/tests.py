from django.test import TestCase
from hello_world__website.models import Person

# Create your tests here.
class ExampleTestClass(TestCase):
    @classmethod
    def setUpTestData(self):
        print('setUpTestData: runs once to set up non-modified test data for all class methods')
        pass

    def setUp(self):
        print('setUp: run once for every test method to setup clean data')
        pass


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(name = 'Benis')

    def test_name_label(self):
        '''
        Test 'Person' model 'name' db column name
        '''
        _person = Person.objects.get(id = 1)
        name_label = _person._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_name_length(self):
        '''
        Test 'Person' model 'name' db column length
        '''
        _person = Person.objects.get(id = 1)
        name_length = _person._meta.get_field('name').max_length
        self.assertEqual(name_length, 128)