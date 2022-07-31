from django.urls import path
from .views import customer, customer_general, bookatable

urlpatterns = [
    path('', customer_general),
    path('<int:number>/', customer),
    path('bookatable', bookatable),
]
