from django.conf.urls import url
from django.urls import path
from . import api
from . import views

urlpatterns = [
    # Testing
    url('test/', api.Test.as_view(), name='test'),
    url('testScript/', views.Test_Script, name='testScript'),

    # Project
    # path('rooms/', views.Rooms_View, name='rooms'),
    path('rooms/', views.Rooms.as_view(), name='rooms'),

    # Movement

    # Status
    path('status/', views.STATUS, name='status'),

    # Traverse Map
    path('traverseMap/', views.traverseMap, name='traverseMap'),
    

]