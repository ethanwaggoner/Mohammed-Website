# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.blog import BlogViewSet
from api.views.comment import CommentViewSet
from api.views.email import ContactFormViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'contact', ContactFormViewSet, basename='contact-form')  # Specify basename

urlpatterns = [
    path('', include(router.urls)),
]
