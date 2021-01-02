from django.urls import path
# from django.conf.urls import url
from . import views

app_name = "chat"
urlpatterns = [
    path('', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]