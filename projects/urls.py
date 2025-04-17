from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.urls import path, include, re_path
from projects import views

router = routers.DefaultRouter()
# router.register(r'login', views.login, 'login')

urlpatterns = [
    path('api/', include(router.urls)),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('users', views.getUsers),
    path('docs/', include_docs_urls(title="Liguilla Api"))
]
