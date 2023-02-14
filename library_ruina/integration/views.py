from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from . import req_bizon
from .models import WebroomTransaction, ViewersImport, TokenImport
from .serializers import WebroomSerializer


def import_bizon():
    webinar_id = "24105:web230622*2023-02-12T19:00:00"
    response_web = req_bizon.request_biz(webinar_id)
    dict_users = response_web.json()
    for user in dict_users["viewers"]:
        viewer = ViewersImport()
        viewer.email = user["email"]
        viewer.phone = user["phone"]
        viewer.view = int(user["viewTill"]) - int(user['view'])
        viewer.buttons = str(user.get("buttons", None))
        viewer.banners = str(user.get("banners", None))
        #viewer.webroom = WebroomTransaction.obgects.get(webinarId=24105:web230622*2023-02-12T19:00:00).id
        viewer.save()
        print(user["username"])
    return HttpResponse('<h1>Okkk</h1>')


class InitialImportAPIView(generics.CreateAPIView):
    model = WebroomTransaction
    serializer_class = WebroomSerializer

