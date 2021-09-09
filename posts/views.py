#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

#Views
posts=[
    {
    'title': 'Aqui nomas',
    'user': 'Luigui',
    'time': datetime.now().strftime('%B %Dth, %Y - %H:M hrs'),
    'picture': 'https://picsum.photos/200/300?random=1',
    },
    {
    'title': 'Relax',
    'user': 'La tortuga',
    'time': datetime.now().strftime('%B %Dth, %Y - %H:M hrs'),
    'picture': 'https://picsum.photos/200/300?random=2',
    },
    {
    'title': 'Having a good time',
    'user': 'Julio',
    'time': datetime.now().strftime('%B %Dth, %Y - %H:M hrs'),
    'picture': 'https://picsum.photos/200/300?random=3'
    },
]

def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <h2><strong>{title}<strong></h2>
            <p><small>{user} - <i>{time}<i></small></p>
            <figure><img src="{picture}"></figure>
            """.format(**post))
    return HttpResponse('<br>'.join(content))
