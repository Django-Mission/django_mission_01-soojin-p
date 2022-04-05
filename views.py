from ast import operator
from multiprocessing import context
from select import select
from tkinter.tix import Select
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def calculator(request):
    #return HttpResponse('계산기 기능 구현 시작합니다.')
    print(f'request type = {request}')
    print(f'request type = {type(request)}')
    print(f'request.__dict__  = {request.__dict__}')

    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    # 3. 응답
    return render(request, 'calculator.html',{'result':result})


#lotto

def lotto(request):
    import random
    num = random.sample(range(1,45),7)
    context = {
        'num':num
    }
    return render(request,'lotto.html',context)
