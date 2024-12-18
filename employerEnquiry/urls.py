from django.urls import path
from .views import EnquiryView

urlpatterns = [
    path('enquiry/', EnquiryView.as_view(), name='enquiry'),
]