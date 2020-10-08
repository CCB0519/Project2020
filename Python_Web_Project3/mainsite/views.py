# from typing import List, Any, Union
#
# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from mainsite.models import Post

from django.template.loader import get_template

from datetime import datetime

from django.shortcuts import redirect

#创建homepage函数用来获取所有文章
def homepage(request):
    #获取模板
    template = get_template('index.html')
    #获取所有数据项
    posts = Post.objects.all()
    #获取当前日期
    now = datetime.now()
    #使用render函数把数据送到指定的模板文件
    html = template.render(locals())
    return HttpResponse(html)
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count+1))+post.title+"<br>")
        post_lists.append("<small>"+post.body+"</small><br><br>")
    return HttpResponse(post_lists)

#创建homeshowpostage函数用来显示单篇文章
def showpost(request,s):
    #获取post.html
    template = get_template('post.html')
    try:
        #根据传入网址查询对应的文章，如果找到则显示文章
        post = Post.objects.get(slug=s)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')