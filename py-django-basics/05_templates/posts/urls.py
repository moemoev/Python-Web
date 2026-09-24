from django.urls import path, include

from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', include(
        [
        path('', views.dashboard, name='dashboard'),
        path('<int:pk>/', views.dashboard_pk, name='dashboard_pk'),
        ])
    ),
    path('custom-tags/', views.dashboard_custom_tags, name='custom-tags'),
]