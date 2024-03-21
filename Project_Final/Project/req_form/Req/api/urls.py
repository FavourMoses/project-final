from django.urls import path
from .import views
app_name = 'Req'
urlpatterns = [
    path('requests/<pk>/', views.RequestListView.as_view(), name='request_list',),
    path('approvals/<pk>/', views.ApproveListView.as_view(), name='request_list',),
    path('user/<pk>/', views.UserListView.as_view(), name='register_user'),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', views.obtain_auth_token, name='obtain_auth_token'),
]