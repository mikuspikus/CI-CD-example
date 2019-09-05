from django.shortcuts import render, HttpResponse
from django.http import HttpRequest, JsonResponse
from hello_world__website.models import Person
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie
def create_person(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        
        if request.POST.get('name'):
            name = request.POST['name']
            person_ = Person.objects.create(name = name)
            person_.save()
            return HttpResponse(person_.id)
        
        else:
            return HttpResponse('\'name\' field must be provided')

    
    else:
        return HttpResponse('POST only controller')

@ensure_csrf_cookie
def list_person(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':

        if request.GET.get('name'):
            name = request.GET['name']
            persons_ = Person.objects.filter(name = name)

            return HttpResponse(', '.join([p_.name for p_ in persons_]))

        else:
            return HttpResponse(', '.join([p_.name for p_ in Person.objects.all()]))

    else:
        return HttpResponse('GET only controller')