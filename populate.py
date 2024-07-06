import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FBVCRUD.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
f=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1,999)
        fename=f.name()
        fesal=randint(10000,20000)
        feaddr=f.city()
        Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
n=int(input('enter no. of employees:'))
populate(n)
print(f'{n} employees inserted succesfully...')