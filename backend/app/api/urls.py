from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.blog import BlogViewSet
from api.views.comment import CommentViewSet
from app import settings

router = DefaultRouter()

router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
