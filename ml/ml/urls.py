from os import stat
from xml.dom.expatbuilder import DOCUMENT_NODE
from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, path


from ml import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('enayat/', views.index, name='index'),
    path('result', views.home, name='home'),
]
