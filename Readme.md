
Это Django-приложение “Образовательные модули”
В нем пользователи могут создавать, получать, менять и удалять образовательные модули или уроки.
Пользователи в этом Django-приложении должны быть авторизованными для получения всех возможностей.
Также в модулях дополнительное поля для иллюстрации сколько всего в каждом модуле находится курсов.
Это приложение поможет достаточно быстро создать образовательные модули.


Инструкции для запуска через Docker 🐋
Настройки окружения

Для успешного запуска проекта необходимо предоставить файл .env, который содержит настройки, описанные в файле .env.example (файл-образец). Перед началом работы следует заполнить значения для описанных переменных согласно потребностям и требованиям проекта.
Структура проекта


Запуск проекта

Чтобы запустить проект через Docker требуется:

    Клонировать этот репозиторий.

    Скопировать переменные из .env.example в .env и установить необходимые значения переменных окружения, как описано в разделе "Настройки окружения".

    Убедиться, что установлены Docker и Docker Compose.

    В командной строке выполнить команду: docker-compose up --build
