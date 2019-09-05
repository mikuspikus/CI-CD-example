from django.conf.urls import url
from hello_world__website.views import create_person, list_person

urlpatterns = [
    url(r'^create-person/', create_person, name = 'create_person'),
    url(r'^list-person/', list_person, name = 'list_person')
]
