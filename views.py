from django.http import HttpResponse
from django.shortcuts import render
import jallery
from . import views



def index(request):
    return HttpResponse("Hello, world. You're at the Jallery Home Page.")


def jalery(request):

    pict_list = jallery.give_me_a_pic_path()
    return HttpResponse(pict_list.__next__())