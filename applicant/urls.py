from django.urls import path
from .views import apply_job, success_page

urlpatterns = [
    path('apply/', apply_job, name='apply_job'),
    path('success/', success_page, name='success_page'),
]
