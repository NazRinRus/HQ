from django.urls import path, include
from study.views import MyLessonsViewSet, MyLessonsByProductViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'my-lessons', MyLessonsViewSet, 'my-lessons')


urlpatterns = [
    path('by-product/<int:product_id>/lessons/', MyLessonsByProductViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]