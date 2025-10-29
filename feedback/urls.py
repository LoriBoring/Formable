from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('feedback_list', views.FeedbackListView.as_view()),
    path('feedback_sent', views.FeedbackSentView.as_view()),
    path('edgar', views.EdgarView.as_view()),
    path('yesgar', views.YesgarView.as_view()),
    path('<int:pk>', views.FieldUpdateView.as_view()),
    path('feedback_list/<int:pk>', views.FeedbackDetailedView.as_view())

]