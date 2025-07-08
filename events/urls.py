from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RegistrationViewSet, register_user, login_user

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')
router.register(r'registrations', RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]
