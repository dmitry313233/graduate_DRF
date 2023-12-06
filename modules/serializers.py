from rest_framework import serializers

from modules.models import Educational, Course
from modules.validators import TitleValidator


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        validators = [
            TitleValidator(field='name'),  # Здесь мы валидируем(настраивалем)поле-name на прописаные нами инструкции('^[a-zA-Z0-9\.\-\ ]+$')
            serializers.UniqueTogetherValidator(fields=['name'], queryset=Course.objects.all())  # Здесь мы делаем делаем уникальным поле-name
        ]


class EducationalSerializer(serializers.ModelSerializer):
    count_course = serializers.SerializerMethodField()  # Создаём переменную для подсчёта курсов
    course_set = CourseSerializer(many=True, read_only=True)  # Вложенность курсов в модуль

    class Meta:
        model = Educational
        fields = '__all__'

    def get_count_course(self, instance):  # Метод для подсчёта количества курсов
        return instance.course_set.all().count()
