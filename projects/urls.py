from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from .views.auth_views import login, register
from .views.users_views import getUsers
from .views.teams_views import GetTeamsView
from .views.categories_views import GetCategoriesView, GetTeamsCategoriesView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('users/', getUsers, name='get_users'),
    path('teams/', GetTeamsView.as_view(), name='get_teams'),
    path('categories/', GetCategoriesView.as_view(), name='get_category'),
    path('teams/categories/', GetTeamsCategoriesView.as_view(), name='add_team_category'),
    path('teams/categories/<int:id_category>/', GetTeamsCategoriesView.as_view(), name='teams_info'),
    path('docs/', include_docs_urls(title="Liguilla Api")),
]