from django.conf.urls import url
from .views import DetailAlunoView



urlpatterns = [
    url(r'minha_view/$', DetailAlunoView.as_view())
]
