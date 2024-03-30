from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.auth import login_user, logout_user, check_session, set_csrf_token
from api.views.blog import BlogViewSet
from api.views.comment import CommentViewSet

router = DefaultRouter()

router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('check-session/', check_session, name='check-session'),
    path('csrf/', set_csrf_token, name='set-csrf-token'),

]