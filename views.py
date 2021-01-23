from django.http import HttpResponse
from django.shortcuts import render
import jallery
from . import views



def index(request):
    return HttpResponse("Hello, world. You're at the Jallery Home Page.")


def test(request):
    list = [1,2,3,4,5,6,7,8,9]
    # jallery.give_me_a_pic_path()
    # list = jallery.pict_list()
    return render(request, "new_app/test.html", {"list": list})