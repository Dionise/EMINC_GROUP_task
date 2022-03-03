from django.urls import path, include

urlpatterns = [
    path('', include('json_csv_app.urls', namespace='json_csv_app')),

]
