from django.db import models


# пользователи, включая авторов продукта и учеников
class Users(models.Model):
    mail = models.EmailField('Почта', unique=True)
    phone = models.CharField('Телефон', max_length=15)
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    author = models.BooleanField('Автор', default=False)# поле определяющее автора продукта, по умолчанию - не автор

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}, surname: {self.surname}, mail: {self.mail}, phone: {self.phone}, author: {self.author}'

class Lesson(models.Model):
    name = models.CharField('Имя', max_length=50)
    video = models.CharField('Видео', max_length=250)
    length_video = models.IntegerField('Длительность видео') # в секундах
    viewing = models.ManyToManyField(Users, through='LessonUsers', related_name='viewing_user')  # пользователи просмотревшие урок

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}, video: {self.video}, length_video: {self.length_video}, viewing: {self.viewing}'

class LessonUsers(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    viewing_time = models.IntegerField('Длительность просмотра')
    viewed = models.BooleanField('Просмотрено', default=False) # показатель просмотра видео

    def __str__(self):
        return f'id: {self.pk}, lesson: {self.lesson}, user: {self.user}, viewing_time: {self.viewing_time}, viewed: {self.viewed}'

    # метод включения Просмотрено
    def on_viewed(self):
        length_video = self.lesson.length_time
        percent_viewed = self.viewing_time * 100 / length_video
        if percent_viewed > 80:
            self.viewed = True
            self.save()

# Сущность продукта
class Product(models.Model):
    name = models.CharField('Имя', max_length=50)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)# автор продукта - ссылка на объект пользователей
    access = models.ManyToManyField(Users, through='ProductUsers', related_name='user_access') # пользователи которым доступен продукт
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE) # ссылка на урок

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}'

class ProductUsers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)