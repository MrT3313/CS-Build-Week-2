from django.conf.urls import url
from django.urls import path
from . import api
from . import views

urlpatterns = [
    # Testing
    url('test/', api.Test.as_view(), name='test'),
    url('testScript/', views.Test_Script, name='testScript'),

    # Project
    url('traverse/', api.Traverse.as_view(), name='traverse'),
    path('rooms/', views.Rooms_View, name='rooms')
]