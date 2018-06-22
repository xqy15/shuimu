from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_user_agents.utils import get_user_agent
# Create your views here.

def index(request):
    #return HttpResponse("<H1>hello world!</H1>")
    ua = get_user_agent(request)
    template_file = 'index.html'
    #if ua.is_mobile or ua.is_tablet:
        #template_file = 'frontend/index_mobile.html'
    return render(request, template_file)

def a(request):
    #return HttpResponse("<H1>hello world!</H1>")
    ua = get_user_agent(request)
    template_file = 'a.html'
    #if ua.is_mobile or ua.is_tablet:
        #template_file = 'frontend/index_mobile.html'
    return render(request, template_file)


def test(request):
    print("A request is received.")
    return JsonResponse({'wahaha': 1})
    #return HttpResponse(json.dumps({"msg":"ok!"}))