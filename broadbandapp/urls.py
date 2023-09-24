from django.urls import path
from . import views

urlpatterns = [
    path('newreg/',views.NewRegsubscribers,name="newsub"),
    path('viewall/',views.viewCustomerDetails,name="viewCus"),
    path('search/',views.SearchDetails,name="SearchCus")
]
