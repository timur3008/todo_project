from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home_page, name='home'),
    path('todos/filter/<str:status>/', views.render_filter_page, name='filter'),
    path('registration/', views.render_registration_form, name='registration'),
    path('authorization/', views.render_authorization_page, name='authorization'),
    path('logout/', views.render_logout_page, name='logout'),
    path('update_todo/<int:todo_id>/<str:action>/', views.render_update_todo_page, name='update_todo'),
    path('search/', views.render_search_page, name='search'),
    path('todo/<int:pk>/update/', views.UpdateTodo.as_view(), name='update'),
    path('profile/', views.render_profile_page, name='profile')
]
