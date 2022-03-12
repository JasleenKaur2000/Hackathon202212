from django.contrib import admin
from django.urls import path


from ml import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('enayat/', views.index, name='index'),
    path('result', views.home, name='home'),
]
