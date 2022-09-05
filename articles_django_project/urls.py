"""articles_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articlesapp.views import home
from articlesapp.views import all_articles
from articlesapp.views import single_article
from articlesapp.views import delete_article
from articlesapp.views import new_article


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('all-articles/', all_articles),
    path('single-article/', single_article),
    path('delete-article/', delete_article),
    path('new-article/', new_article),
]

