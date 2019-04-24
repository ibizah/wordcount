from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
def say(request):
    return HttpResponse('<em>hello ibi <em/><br/><h1>I am gold<h1/>')



def homepage(request):
    return render(request,'home.html',{'a':'Hello World'})


def count(request):
    s1=request.GET['fulltext']

    count= len(s1.split(' '))
    s=s1.split(' ')
    cnt=Counter(s)
    l=[]
    for k,v in cnt.items():
         l.append([v,k])
    max_count=max(l)[1]
    print(max_count)
    fname=request.GET['fname']
    email=request.GET['email']
    pno=request.GET['pno']

    return render(request,'count.html', {'count':count, 'maxcount':max_count, 'string':s1,'cnt':cnt.items(),
                                          'fname':fname, 'email':email, 'pno':pno})


def help(request):
    return render(request,'help.html')

def check(request):
    return render(request,'check.html')
