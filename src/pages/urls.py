from django.urls import path

from .views import homePageView, writeView, deleteView

urlpatterns = [
    path('', homePageView, name='home'),
    path('write/', writeView, name="write"),
    path('delete/', deleteView, name="delete")
]
