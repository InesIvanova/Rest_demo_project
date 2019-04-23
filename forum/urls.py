from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^questions/$', views.QuestionsList.as_view(), name='questions'),
    re_path('^questions/(?P<question_id>\d+)/$', views.QuestionDetails.as_view(), name='question-details'),
    re_path('^users/questions/$', views.UserList.as_view(), name='question-details')

]