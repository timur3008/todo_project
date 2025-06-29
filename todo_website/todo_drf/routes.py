# from rest_framework import routers
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.urls import path

from . import views


# router = routers.DefaultRouter()
# router.register(prefix='todos', viewset=views.TodoViewSet, basename='todos')

schema_view = get_schema_view(
    info=openapi.Info(title='Todo API', default_version='v1'), 
    public=True, 
    permission_classes=(permissions.AllowAny, )
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),

    # path('api-drf/todos/', views.TodoListCreateView.as_view(), name='todos'),
    # path('api-drf/todos/<int:pk>', views.TodoDetailView.as_view(), name='todo_detail'),

    path('api-drf/todos/', views.TodoListView.as_view(), name='todos'),
    path('api-drf/todos/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('api-drf/todos/create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('api-drf/update/todos/<int:pk>/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('api-drf/patch/todos/<int:pk>/', views.TodoPatchView.as_view(), name='todo_patch'),
    path('api-drf/delete/todos/<int:pk>/', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('api-drf/user/register/', views.RegisterView.as_view(), name='register_user'),
    path('api-drf/user/login/', views.LoginView.as_view(), name='login_user'),
]