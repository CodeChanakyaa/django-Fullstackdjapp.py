from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', Blog_API_L.as_view()),

    path('blog/<int:pk>', Blog_API_R.as_view()),

    path('comments/', Comment_API_CL.as_view()),

    path('comments/<int:pk>', Comment_API_RUD.as_view()),

    path('contact/', Contact_API_C.as_view()),
]
