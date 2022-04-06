from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(Home.as_view()), name='home'),
    path('contact/', contact, name='contact'),
]
