from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/users/', views.UserList.as_view(),name='users'),
    path('api/users/<pk>/', views.UserDetail.as_view(),name='userdetail'),
    path('api/appointments', views.Appointments.as_view(), name='appointments'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/response/', views.ResponseList.as_view(), name='responses')
]

urlpatterns = format_suffix_patterns(urlpatterns)


