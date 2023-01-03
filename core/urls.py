from django.urls import path
from .views import IndexView, ProjetosView, ModalView, CurriculoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projetos', ProjetosView.as_view(), name='projetos'),
    path('modal', ModalView.as_view(), name='modal'),
    path('curriculo', CurriculoView.as_view(), name='curriculo'),
]