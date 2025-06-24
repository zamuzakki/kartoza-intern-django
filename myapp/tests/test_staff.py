from django.test import TestCase
from myapp.models import State, Staff
from myapp.tests.factories import StateFactory, StaffFactory

class TestStaff(TestCase):
    """
    Test Staff object
    """

    @classmethod
    def setUpTestData(cls):
        """
        Run once to set up non-modified test data.
        This is usually data that are shared across all test methods.
        """
        # state = State.objects.create(
        #     name='State 1',
        #     population=1000
        # )
        # staff = Staff.objects.create(
        #     name='John Doe',
        #     age=25,
        #     sex='M',
        #     salary=10000,
        #     address='123 Main St',
        #     state_id=state.id
        # )

        state = StateFactory.create()
        staff = StaffFactory.create(state=state)

    def setUp(self) -> None:
        """
        Run once for every test method.
        This is for data that could be modified during the test.
        """
        pass

    def test_one_plus_one_equals_two(self):
        """
        Test that 1 + 1 equals 2.
        """
        self.assertEqual(1 + 1, 2)
