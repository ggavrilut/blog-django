from django.urls import path
from front.views import HomeView, AboutView, homeContent

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'), 
    path('content/<str:value>', homeContent, name="home_content"),
    path('about', AboutView.as_view(), name='about')
]
