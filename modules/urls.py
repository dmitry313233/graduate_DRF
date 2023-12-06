from django.urls import path
from rest_framework.routers import DefaultRouter

from modules.apps import ModulesConfig
from modules.views import EducationalViewSet, CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, \
    CourseUpdateAPIView, CourseDestroyAPIView

app_name = ModulesConfig.name

router = DefaultRouter()
router.register(r'module', EducationalViewSet, basename='module')

urlpatterns = [
    path('course/create/', CourseCreateAPIView.as_view(), name='course/create'),
    path('course/', CourseListAPIView.as_view(), name='course'),
    path('course/retrieve/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course/retrieve'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course/update'),
    path('course/destroy/<int:pk>/', CourseDestroyAPIView.as_view(), name='course/destroy')
] + router.urls
