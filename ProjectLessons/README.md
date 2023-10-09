# Тестовое задание HQ. Проект ProjectLesson

# 1. Создание виртуального окружения:
python3 -m venv venv_hq
# 2. Активировать виртуальное окружение:
source venv_hq/bin/activate
# 3. Установка django:
pip3 install django
# 4. Создание проекта ProjectLesson:
django-admin startproject ProjectLesson
# 5. Создание приложения lessons:
cd ProjectLessons
python3 manage.py startapp lessons

*установка Django Rest Framework:*
`pip install djangorestframework`

# 7. Задание:


    1. Построение архитектуры(3 балла)


    1.1. Создать сущность продукта. У продукта должен быть владелец. Необходимо добавить сущность для сохранения доступов к продукту для пользователя.
    1.2. Создать сущность урока. Урок может находиться в нескольких продуктах одновременно. В уроке должна быть базовая информация: название, ссылка на видео, длительность просмотра (в секундах).
    1.3. Урок могут просматривать множество пользователей. Необходимо для каждого фиксировать время просмотра и фиксировать статус “Просмотрено”/”Не просмотрено”. Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.


    2. Написание запросов(7 баллов)


    2.1. Реализовать API для выведения списка всех уроков по всем продуктам к которым пользователь имеет доступ, с выведением информации о статусе и времени просмотра.
    2.2. Реализовать API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ, с выведением информации о статусе и времени просмотра, а также датой последнего просмотра ролика.
    2.3. Реализовать API для отображения статистики по продуктам. Необходимо отобразить список всех продуктов на платформе, к каждому продукту приложить информацию:
        a. Количество просмотренных уроков от всех учеников.
        b. Сколько в сумме все ученики потратили времени на просмотр роликов.
        c. Количество учеников занимающихся на продукте.
        d. Процент приобретения продукта (рассчитывается исходя из количества полученных доступов к продукту деленное на общее количество пользователей на платформе).


# Реализация:

1. файл models.py

2.1. http://127.0.0.1:8000/api/v1/exercise1/<pk>/

2.2. http://127.0.0.1:8000/api/v1/exercise2/1/?access__mail=mail2@example.com

2.3. http://127.0.0.1:8000/api/v1/exercise2/