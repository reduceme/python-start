# coding:utf-8
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request):
    string = u"这是一个字符串模板"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(100))
    return render(request, 'index.html', {'string': string, 'TutorialList': TutorialList, 'info_dict': info_dict, 'List': List})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = ini(a) + ini(b)
    return HttpRequest(str(c))