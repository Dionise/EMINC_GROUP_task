from django.urls import path

from .views import HomeView


app_name = 'json_csv_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]