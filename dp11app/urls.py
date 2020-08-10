from django.urls import path
from dp11app import views

app_name="dp11app"


urlpatterns=[
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]