from django.urls import path
from . import views
from chat.views import ChatView
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('/profile', views.profile),
    path('/profile/edit',csrf_exempt(ChatView.as_view())),
    path('/message', views.message)
]