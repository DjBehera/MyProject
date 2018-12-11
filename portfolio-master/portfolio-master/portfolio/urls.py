"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import getcsv.views
import master.views
import excel.views
import consolify.views
import catsndogs.views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/',jobs.views.home,name = 'home'),
	path('blog/',include('blog.urls')),
	path('excel/',excel.views.task,name='excel'),
	path('getcsv/',getcsv.views.task,name='getcsv'),
	path('master/',master.views.task,name='master'),
	path('consolify/',consolify.views.task,name='consolify'),
	path('catsndogs/',catsndogs.views.task,name='catsndogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
