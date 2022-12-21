from django.urls import path
from .views import IndexView, ProjetosView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projetos', ProjetosView.as_view(), name='projetos'),
]