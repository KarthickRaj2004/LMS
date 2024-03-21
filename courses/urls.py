# courses/urls.py

from django.urls import path
from .views import course_list, course_detail, sub_course_detail, payment_page  # Import payment_page view function
from . import views  # Import views module from the same directory


urlpatterns = [
    path('', course_list, name='course_list'),  
    path('<int:course_id>/', course_detail, name='course_detail'),  
    path('sub_course/<int:sub_course_id>/', sub_course_detail, name='sub_course_detail'),  # New URL pattern
    path('payment/', payment_page, name='payment_page'),  # URL pattern for payment_page

    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('contact', views.contact, name='contact'), 
]
