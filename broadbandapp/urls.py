from django.urls import path
from . import views

urlpatterns = [
    path('newreg/',views.NewRegsubscribers,name="newsub")
]
