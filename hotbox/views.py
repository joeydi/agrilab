import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.serializers.json import DjangoJSONEncoder
from .models import Source, Reading

def index(request):
    response = JsonResponse(readings)

def readings(request, source_id):
    date = datetime.date.today()
    source = get_object_or_404(Source, pk=source_id)
    readings = Reading.objects.filter(source=source, date__contains=date)
    data = [r.data for r in readings]
    return JsonResponse({'data': data})
