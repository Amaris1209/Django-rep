from django.urls import path
from myapp.views import PostList, PostDetail
from django.urls import path
from .swagger import schema_view

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

