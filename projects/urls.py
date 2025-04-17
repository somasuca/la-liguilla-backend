from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.urls import path, include, re_path
from .views.auth_views import login, register
from .views.users_views import getUsers

router = routers.DefaultRouter()
# router.register(r'login', views.login, 'login')

urlpatterns = [
    re_path('login', login),
    re_path('register', register),
    re_path('users', getUsers),
    path('docs/', include_docs_urls(title="Liguilla Api"))
]
