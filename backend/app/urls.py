from django.conf.urls import url
from django.urls import path
from . import api
from . import views

urlpatterns = [
    url('test/', api.Test.as_view(), name='test'),
    url('traverse/', api.Traverse.as_view(), name='traverse'),
    # url('rooms/', api.GetRooms.as_view(), name='rooms'),
    path('rooms/', views.Room_View, name='rooms')
]