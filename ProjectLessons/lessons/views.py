from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from  rest_framework import viewsets

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        result = {}
        user = get_object_or_404(queryset, pk=pk)
        result['user'] = self.serializer_class(user).data
        lessons = LessonUsers.objects.filter(user=user )
        result['lessons'] = []
        for lesson in lessons:
            les = LessonUsersSerializer(lesson).data
            les['name'] = lesson.lesson.name
            les['video'] = lesson.lesson.video
            les['length_video'] = lesson.lesson.length_video
            les['product']=[]
            products = Product.objects.filter(access=user)
            for product in products:
                prod = ProductSerializer(product).data
                print('test', product)
                les['product'].append({'name': product.name})
            print('test les:', les)
            result['lessons'].append(les)
            print('test', result)
        return Response(result)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Меняем кверисет под фильтрацию по пользователю
    def get_queryset(self):
        queryset = Product.objects.all()
        user = self.request.query_params.get('access__mail', None)
        if user is not None:
            queryset = queryset.filter(access__mail=user)
        return queryset

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        result = {}
        product = get_object_or_404(queryset, pk=pk)
        user = self.request.query_params.get('access__mail', None)
        result['product'] = self.serializer_class(product).data.pop('lesson')
        lesson = LessonSerializer(product.lesson).data
        lesson_user = LessonUsers.objects.get(lesson=product.lesson, user__mail=user)
        lesson['viewing']=LessonUsersSerializer(lesson_user).data
        result['lesson'] = lesson
        return Response(result)

    def list(self, request):
        queryset = self.queryset
        products = self.serializer_class(queryset, many=True).data
        result = {}
        result['product'] = products
        for product in result['product']:
            viewing_objects = LessonUsers.objects.filter(lesson=product['lesson']['pk'])
            product['lesson']['viewing']=[]
            for viewing in viewing_objects:
                product['lesson']['viewing'].append({'viewing_time': viewing.viewing_time, 'viewed': viewing.viewed,
                                                    'user': viewing.user.mail})
        return Response(result)

class LessonUsersViewSet(viewsets.ModelViewSet):
    queryset = LessonUsers.objects.all()
    serializer_class = LessonUsersSerializer