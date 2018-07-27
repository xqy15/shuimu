from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_user_agents.utils import get_user_agent
# Create your views here.

def index(request):
    #return HttpResponse("<H1>hello world!</H1>")
    ua = get_user_agent(request)
    template_file = 'frontend/index.html'
    #if ua.is_mobile or ua.is_tablet:
        #template_file = 'frontend/index_mobile.html'
    return render(request, template_file)

def aboutus(request):
    #return HttpResponse("<H1>hello world!</H1>")
    ua = get_user_agent(request)
    template_file = 'frontend/aboutus.html'
    #if ua.is_mobile or ua.is_tablet:
        #template_file = 'frontend/index_mobile.html'
    return render(request, template_file)


def test(request):
    print("A request is received.")
    return JsonResponse({'wahaha': 1})
    #return HttpResponse(json.dumps({"msg":"ok!"}))

def page1(request):
    return render(request, 'page1.html')

def page3(request):
    return render(request, 'page3.html')

def page51(request):
    return render(request, 'page51.html')

def page52(request):
    return render(request, 'page52.html')

def page7(request):
    return render(request, 'page7.html')