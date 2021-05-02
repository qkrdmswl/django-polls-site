"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include    # path install 문제
from home import views as v1
from accounts import views as v2
from django.conf.urls import url, include

urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('polls/<int:question_id>/', v1.detail, name='detail'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
