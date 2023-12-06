from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Course, Educational
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='skypro',
            email='skypro@mail.ru'
        )

        self.educational = Educational.objects.create(
            name='test',
            description='test',
            owner=self.user
        )

        self.course = Course.objects.create(
            name='python',
            description='test',
            owner=self.user,
            educational=self.educational
        )

        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        """Тестирование создания курса"""
        data = {'name': 'test', 'description': 'test', 'owner': self.user.pk, 'educational': self.educational.pk}
        response = self.client.post(
            reverse('modules:course/create'), data=data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 6, 'name': 'test', 'description': 'test', 'amount': 70000, 'owner': 5, 'educational': 5}
        )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_course_list(self):
        """Тестирование получения списка курса"""
        response = self.client.get(
            reverse('modules:course')
        )

        # print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [{'id': 2, 'name': 'python', 'description': 'test', 'amount': 70000, 'owner': 2, 'educational': 2}]
        )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_course_retrieve(self):
        """Тестирование получение элемента курса"""
        response = self.client.get(
            reverse('modules:course/retrieve', args=[self.course.pk])
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_course_update(self):
        """Тестирование обновления курса"""
        update_data = {'id': self.course.id, 'name': 'test', 'description': 'test', 'owner': self.user.pk,
                       'educational': self.educational.pk}
        response = self.client.put(
            reverse('modules:course/update', args=[self.course.pk]),
            data=update_data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['name'], 'test'
        )

        self.assertTrue(
            Course.objects.filter(pk=self.course.pk).exists()
        )

    def test_course_delete(self):
        """Тестирование на удаление курса"""
        response = self.client.delete(
            reverse('modules:course/destroy', args=[self.course.pk])
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )


class EducationalTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='skypro',
            email='skypro@mail.ru'
        )

        self.educational = Educational.objects.create(
            name='test',
            description='test',
            owner=self.user
        )

        self.course = Course.objects.create(
            name='python',
            description='test',
            owner=self.user,
            educational=self.educational
        )

        self.client.force_authenticate(user=self.user)

    def test_educational_create(self):
        """Тестирование создания модуля"""
        data = {'number': self.educational.pk, 'name': 'test', 'description': 'test', 'owner': self.user.pk}
        response = self.client.post(
            '/module/', data=data
        )

        #print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 7, 'count_course': 0, 'course_set': [], 'number': 6, 'name': 'test', 'description': 'test',
             'amount': 70000, 'owner': 6}
        )

        self.assertTrue(
            Educational.objects.all().exists()
        )

    def test_educational_list(self):
        """Тестирование на получение списка модуля"""
        response = self.client.get(
            '/module/'
        )

        #print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(), [{'id': 9, 'count_course': 1, 'course_set': [
                {'id': 9, 'name': 'python', 'description': 'test', 'amount': 70000, 'owner': 8, 'educational': 9}],
                               'number': 0, 'name': 'test', 'description': 'test', 'amount': 70000, 'owner': 8}]
        )

        self.assertTrue(
            Educational.objects.all().exists()
        )

    def test_educational_retrieve(self):
        """Тестирование получение элемента модуля"""
        response = self.client.get(
            '/module/', args=[self.educational.pk]
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_educational_update(self):
        """Тестирование получение элемента модуля"""
        update_data = {'id': self.educational.id, 'name': 'test', 'description': 'test', 'owner': self.user.pk}
        response = self.client.put(
            f'/module/{self.educational.pk}/',
            data=update_data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()['name'], 'test'
        )

        self.assertTrue(
            Educational.objects.filter(pk=self.educational.pk).exists()
        )

    def test_educational_delete(self):
        """Тестирование получение элемента модуля"""
        #print(f'{self.educational = }')
        response = self.client.delete(
            f'/module/{self.educational.pk}/',
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
