from django.test import TestCase
from myapp.tests.factories import StateFactory, StaffFactory, LakeFactory
from myapp.models import State, Staff, Lake


class ModelFactoryTest(TestCase):
    def test_state_factory(self):
        state = StateFactory()
        self.assertIsInstance(state, State)
        self.assertTrue(state.name)
        self.assertIsNotNone(state.population)

    def test_staff_factory(self):
        staff = StaffFactory()
        self.assertIsInstance(staff, Staff)
        self.assertTrue(staff.name)
        self.assertIn(staff.sex, ['M', 'F'])
        self.assertIsInstance(staff.state, State)

    def test_lake_factory(self):
        lake = LakeFactory()
        self.assertIsInstance(lake, Lake)
        self.assertTrue(lake.name)

    def test_create_multiple_objects(self):
        # Create multiple objects at once
        states = StateFactory.create_batch(5)
        self.assertEqual(len(states), 5)

        staffs = StaffFactory.create_batch(10)
        self.assertEqual(len(staffs), 10)
