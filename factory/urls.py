from django.urls import path
from factory.views import CreateOrder

urlpatterns = [
    path('create-order', CreateOrder.as_view())
]