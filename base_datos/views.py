from django.shortcuts import render
from django.views.generic import View
from .models import UsoCpu,UsoMemoria
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class cpu_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pid=0):
        if (pid > 0):
            res=list(UsoCpu.objects.filter(pid=pid).values())
            if len(res) > 0:
                respons= res[0]
                data = {'process': respons}
            else:
                data = {'process': 'process not found'}
            return JsonResponse(data)
        else:
            res = list(UsoCpu.objects.values())
            if len(res) > 0:
                data = {'process_list': res}
            else:
                data = {'message': 'no processes found'}

            return JsonResponse(data)

class memory_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pid=0):
        if (pid > 0):
            res=list(UsoMemoria.objects.filter(pid=pid).values())
            if len(res) > 0:
                respons= res[0]
                data = {'process': respons}
            else:
                data = {'process': 'process not found'}
            return JsonResponse(data)
        else:
            res = list(UsoMemoria.objects.values())
            if len(res) > 0:
                data = {'process_list': res}
            else:
                data = {'message': 'no processes found'}

            return JsonResponse(data)
