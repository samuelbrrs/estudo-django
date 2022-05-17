from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from users import views as usersviews

routes = routers.DefaultRouter()
routes.register('user', usersviews.UsersViewSet, basename = 'Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('', include(routes.urls)),
]