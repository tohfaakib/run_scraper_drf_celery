from django.shortcuts import HttpResponse
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .serializers import TriggerSerializer
from background_runner.task import sleepy, start_tracking



def index(request):
    sleepy.delay(30)
    return HttpResponse("<h1>hi</h1>")


class Entry(object):
    def __init__(self, **kwargs):
        for field in ('start_url', 'start_page_number',):
            setattr(self, field, kwargs.get(field, None))


class TriggerProcess(viewsets.ViewSet):
    serializer_class = TriggerSerializer

    def list(self, request):
        start_url = str(request.data['start_url'])
        start_page_number = str(request.data['start_page_number'])

        print(start_url)
        print(start_page_number)
        if start_url and start_page_number:
            print("calling..")
            start_tracking.delay(start_url, start_page_number)
            # start_tracking(start_url, start_page_number)

        entries = {
            1: Entry(start_url=start_url, start_page_number=start_page_number),
        }
        serializer = TriggerSerializer(instance=entries.values(), many=True)
        return Response({'success': True, 'message': 'tracking started successfully.'})


