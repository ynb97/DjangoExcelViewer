from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(
        'getfile/', 
        views.get_file_by_name, 
        name='get-file'
        ),
    path(
        'sendfile/', 
        views.send_file, 
        name='send-file'
        ),
]