from django.http import HttpResponse

from datetime import datetime

def message(request):
    now = datetime.now()
    return HttpResponse('Aquí encontraran un espacio para compartir sus ideas. Fecha: {now}'.format(now=str(now)))
