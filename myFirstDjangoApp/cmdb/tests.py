# -*- coding: utf-8 -*-

# from django.http import HttpResponse
#
# from cmdb.models import Test
#
#
# # 数据库操作
# def testdb(request):
#     test1 = Test(name='reg')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")

from django.http import HttpResponse
from cmdb.models import Test

def testdb(request):
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于sql中的select * from
    list = Test.objects.all()

    # filter相当于sql中的where，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获得单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据，相当于sql中的offset 0 limit 2
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="reg").order_by("id")

    for var in list:
        response1 += var.name + " "

    response = response1
    return HttpResponse(response)