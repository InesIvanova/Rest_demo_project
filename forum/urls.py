from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^questions/$', views.QuestionsList.as_view(), name='questions')
]