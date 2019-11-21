from django.urls import path
from front.views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'), 
    path('about', AboutView.as_view(), name='about')
]
