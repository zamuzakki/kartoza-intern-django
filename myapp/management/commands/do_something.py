from django.core.management.base import BaseCommand
from myapp.models import Staff, State
from django.db.models import Q



class Command(BaseCommand):
    help = 'Do something'

    def handle(self, *args, **options):
        # Will return the record as 1 object
        state_1 = State.objects.get(id=1)
        # print(state_1)

        # # query all objects
        # print(State.objects.all())

        # # Order
        # print(State.objects.order_by('population', '-name'))

        # # State.objects.first()
        # # State.objects.all().first()
        # print(State.objects.first())
        # print(State.objects.last())

        # print(
        #     State.objects.filter(name='State 2')
        # )
        # print(
        #     State.objects.filter(name='State 3')
        # )
        # print(
        #     State.objects.filter(population=1000)
        # )
        # print(
        #     State.objects.filter(population__gt=1000)
        # )
        # print(
        #     State.objects.filter(
        #         name__istartswith='st',
        #         population__gte=1000
        #     )
        # )

        # print(
        #     State.objects.filter(
        #         Q(name='State 2') | Q(name='State 1')
        #     )
        # )
        # print(
        #     State.objects.filter(
        #         name__in=['State 2', 'State 1']
        #     )
        # )

        # print(
        #     State.objects.values('name')
        # )
        # print(
        #     State.objects.values_list('name', 'population')
        # )
        # print(
        #     State.objects.values_list('name')
        # )
        # print(
        #     State.objects.values_list('name', flat=True)
        # )




        # use state_id
        print(Staff.objects.values_list('name', flat=True))

        # staff_1 = Staff.objects.create(
        #     name='John Doe',
        #     age=30,
        #     address='123 Main St',
        #     salary=50000,
        #     sex='M',
        #     state_id=1
        # )
        # print(Staff.objects.values_list('name', flat=True))

        # staff_2 = Staff(
        #     name='Jane Dee',
        #     age=30,
        #     address='123 Main St',
        #     salary=50000,
        #     sex='M',
        #     state=state_1
        # )
        # print(staff_2.id)
        # staff_2.save()
        # print(staff_2.id)
        # print(Staff.objects.values_list('name', flat=True))

        # staff_3 = Staff.objects.create(
        #     name='Akbar',
        #     age=30,
        #     address='123 Main St',
        #     salary=50000,
        #     sex='M',
        #     state=None
        # )
        # print(f"State: {staff_3.state}")

        staff_3 = Staff.objects.filter(name='Akbar').first()
        print(staff_3.state)
        print(staff_3.state_id)

        staff_3.state = state_1
        staff_3.state_id = state_1.id
        print(staff_3.state)
        print(staff_3.state_id)

        staff_3.save()
        print(staff_3.state)
        print(staff_3.state_id)

        staff_3.delete()

        Staff.objects.all().delete()