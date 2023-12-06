from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from modules.models import Educational, Course
from modules.paginations import CoursePaginator
from modules.serializers import EducationalSerializer, CourseSerializer


class EducationalViewSet(viewsets.ModelViewSet):
    """View set для модуля"""
    serializer_class = EducationalSerializer
    queryset = Educational.objects.all()
    permission_classes = [AllowAny]  # Это права доступа на модуль  # Было [IsAuthenticated]


class CourseCreateAPIView(generics.CreateAPIView):
    """Создание курса"""
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]  # Было [IsAuthenticated]

    def perform_create(self, serializer):  # Для сохранения владельца
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class CourseListAPIView(generics.ListAPIView):
    """Список курсов"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """Детали курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseUpdateAPIView(generics.UpdateAPIView):
    """Редактирование курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDestroyAPIView(generics.DestroyAPIView):
    """Удаление курса"""
    #serializer_class = CourseSerializer  # Здесь не нужен сериализатор так как мы ничего не отправляем!
    queryset = Course.objects.all()

