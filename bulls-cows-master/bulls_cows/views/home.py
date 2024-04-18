from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages

from bulls_cows.common.functionality import test_cooke

def home(request):
    #todo - make better cookie message

    cookie_state = test_cooke(request)

    context = {
        "item": 1,
        "cookie_state": cookie_state,
    }

    request.session.set_test_cookie()

    return render(request, 'home.html', context)


def about(request):
    
    cookie_state = test_cooke(request)

    context = {
        "item": 1,
        "cookie_state": cookie_state,
    }
    
    request.session.set_test_cookie()

    return render(request, 'about.html', context)