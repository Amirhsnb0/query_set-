from itertools import count
from typing import Annotated
from django.db.models import F, Sum, Count, Case, When
from .models import *


def query_0():
    q = Employee.objects.all()
    return q
    

def query_1():
    dic={}
    q = Employee.objects.all()
    price = Salary.objects.annotate(Sum('base','tax','insurance','overtime'))
    dic["total_dept"]=price

    return dic
   
    


def query_2(x):
    dic={}
    if x>= 20 :
        price=Salary.objects.annotate(Sum('overtime'))
        dic["total_overtime"]=price
    print(dic)

    

def query_3():
    dic={}
    price = Payment.objects.annotate(Sum('amount'))
    dic['value']= price
    print(dic)



def query_4(request,x):
    acc=EmployeeProjectRelation.objects.get(pk=x)
    print(acc.hours)

    
    pass


def query_5(x):
    # TODO
    pass


def query_6():
    # TODO
    pass


def query_7():
    # TODO
    pass


def query_8():
    # TODO
    pass


def query_9(x):
    # TODO
    pass


def query_10():
    # TODO
    pass
