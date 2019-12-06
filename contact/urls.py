from django.urls import path
from contact.views import ContactFormV2View, contactSimpleView, ContactViewV1

urlpatterns = [
    path('', contactSimpleView, name='contact'), 
    path('v1/', ContactViewV1.as_view(), name='contact_v1'), 
    path('v2/', ContactFormV2View.as_view(), name='contact_v2')
]
