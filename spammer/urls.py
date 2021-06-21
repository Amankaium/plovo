from django.urls import path
from .views import main, success

urlpatterns = [
    path("", main, name="email-main"),
    path("success/", success, name="email-success"),
]