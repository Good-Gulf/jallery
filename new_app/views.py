from django.shortcuts import render
import jallery

pict_list = jallery.pict_list


def test(request):
    jallery.give_me_a_pic_path()
    pict_list = jallery.pict_list
    return render(request, "new_app/test.html", {"pict_list": jallery.pict_list})
