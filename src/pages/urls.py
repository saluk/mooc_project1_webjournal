from django.urls import path

from .views import homePageView, writeView

urlpatterns = [
    path('', homePageView, name='home'),
    path('write/', writeView, name="write")
]
