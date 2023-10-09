from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('mail', 'phone', 'name', 'surname', 'author')
    # при сохранении пользователя, проверяем по емайлу его наличие в БД, если есть то возвращаем уже сохраненного, инача сохраняем нового
    def save(self, **kwargs):
        self.is_valid()
        user = Users.objects.filter(mail=self.validated_data.get('mail'))
        print('test', self.validated_data.get('mail'))
        if user.exists():
            return user.first()
        else:
            new_user = Users.objects.create(
                surname=self.validated_data.get('surname'),
                name=self.validated_data.get('name'),
                author=self.validated_data.get('author'),
                phone=self.validated_data.get('phone'),
                mail=self.validated_data.get('mail'),
            )
            return new_user




class LessonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    video = serializers.CharField(required=False)
    length_video = serializers.IntegerField(required=False) # в секундах
    #viewing = LessonUsersSerializer(required=False, many=True)

    class Meta:
        model = Lesson
        fields = ('pk', 'name', 'video', 'length_video', 'viewing')

class LessonUsersSerializer(serializers.ModelSerializer):
    viewing_time = serializers.IntegerField(required=False)
    viewed = serializers.BooleanField(required=False)


    class Meta:
        model = LessonUsers
        fields = ('viewing_time', 'viewed')

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    lesson = LessonSerializer(required=False)
    class Meta:
        model = Product
        fields = ('name', 'lesson')
