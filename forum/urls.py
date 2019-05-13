from django.urls import re_path, path
from . import views


urlpatterns = [
    path('questions/', views.QuestionsList.as_view(), name='questionss'),
    re_path('^questions/(?P<question_id>\d+)/$', views.QuestionDetails.as_view(), name='question-details'),
    re_path('^users/questions/$', views.UserList.as_view(), name='question-details')

]