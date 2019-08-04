from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('community/',views.community,name='community'),
    path('about',views.about,name="about")
]
