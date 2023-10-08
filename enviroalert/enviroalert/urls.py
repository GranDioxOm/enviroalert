"""
URL configuration for enviroalert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from web import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', views.IndexView.as_view(), name='index'),
    path('fire-main', views.FireView.as_view(), name='fire-main'),
    path('fire-map', views.FireMap.as_view(), name='fire-map'),
    path('fire-learn', views.FireLearn.as_view(), name='fire-learn'),
    path('fire-report', views.FireReport.as_view(), name='fire-report'),
    path('fire-report-2', views.FireReport2.as_view(), name='fire-report-2'),
    path('fire-report-3', views.FireReport3.as_view(), name='fire-report-3'),
    path('fire-report-4', views.FireReport4.as_view(), name='fire-report-4'),
    path('fire-report-5', views.FireReport5.as_view(), name='fire-report-5'),
    path('fire-report-6', views.FireReport6.as_view(), name='fire-report-6'),
]
urlpatterns += staticfiles_urlpatterns()
