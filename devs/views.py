from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        # return HttpResponse(content='Hola mundo desde Django')
        data = {
            'name': 'Luis Bohorquez',
            'years': 23,
            'skills': ['python', 'Laravel', 'React', 'Angular']
        }
        return render(request, 'Hello_world.html', context=data)