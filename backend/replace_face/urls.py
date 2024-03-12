from django.urls import path
from .views import replace_face, get_video

urlpatterns = [
    path('replace-face/', replace_face, name='replace_face'),
    path('get_video/<str:video_name>/', get_video, name='get_video'),
    # path('get_video/', get_video, name='get_video')
]
