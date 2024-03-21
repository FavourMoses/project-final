from django.urls import path, include
from .import views
from django.contrib.auth.views import LogoutView
app_name = 'Req'
urlpatterns = [
     path('login/', views.user_login, name='login'),
     path('approve/<int:request_id>/', views.approve_requisition, name='approve_requisition'),
     path('submit/', views.submit_requisition, name='submit_requisition'),
     path('logout/', views.custom_logout, name='logout'),
     path('approval_email/', views.send_approval_email, name='send_approval_email')

]