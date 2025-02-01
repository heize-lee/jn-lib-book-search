from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_and_save_call_numbers, name='scrape_call_numbers'),
]
