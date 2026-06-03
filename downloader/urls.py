from django.urls import path
from . import views

app_name = 'downloader'

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', views.analyze_video, name='analyze_video'),
    path('download/', views.download_file, name='download_file'),
]
