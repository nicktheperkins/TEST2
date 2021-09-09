"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# this imports the url pattern to be used
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Django Part 10 Code
from django.contrib import admin
from django.urls import path
from . import views # Django Part 6 Code

urlpatterns = [
    # Anatomy of a URL route:
    # ('pattern to watch for', method to call, "shortcut name")
    path('', views.home, name="home"), # Django Part 6 Code
    path('admin/', admin.site.urls),
]
# this says to add whatever is put into the staticfiles_urlpatterns back into the variable
urlpatterns += staticfiles_urlpatterns() # Django Part 10 Code
