from django.http import HttpResponse

from datetime import datetime

import json

def message(request):
    return HttpResponse('Aquí encontraran un espacio para compartir sus ideas. Fecha: {now}'.format(
    now=datetime.now().strtime('%b / %d / %y - %h:%m hrs')))

def challenge(request):
    numbers = [int(n) for n in request.GET['numbers'].split(',')]
    sorted_list = sorted(numbers)
    data = {
        'status': 'Ok',
        'numbers': sorted_list,
        'message': 'list sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def access(request, name, age):
    if age < 18:
        message = 'Sorry, {} You dont have access'.format(name)
    else:
        message = 'Hi, {} welcome to astrofotografia'.format(name)

    return HttpResponse(message)
