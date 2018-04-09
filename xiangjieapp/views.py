from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import News,Question
from datetime import datetime
from datetime import datetime

from django.http import HttpResponse
from django.template.loader import get_template

from .models import News


# Create your views here.

def index(request):
    template = get_template('index.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def newsshowall(request):
    template = get_template('news.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def newsshow(request,slug):
    template = get_template('onenews.html')
    try:
        new = News.objects.get(slug=slug)
        if new != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')


def questionshowall(request):
    template = get_template('question.html')
    questions = Question.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def questionshow(request,slug):
    template = get_template('onequestion.html')
    try:
        question = Question.objects.get(slug=slug)
        if question != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def product(request):
    template = get_template('product.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def danwendankong(request):
    template = get_template('danwendankong.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def shuangwenshuangkong(request):
    template = get_template('shuangwenshuangkong.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def jiguikongtiao(request):
    template = get_template('jiguikongtiao.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def hengwena(request):
    template = get_template('hengwena.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def hengwenb(request):
    template = get_template('hengwenb.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def haixianji(request):
    template = get_template('haixianji.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def about(request):
    template = get_template('about.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def honor(request):
    template = get_template('honor.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def contact(request):
    template = get_template('contact.html')
    news = News.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
