import imp
from django.contrib import admin
from django.urls import path,include

import mainWebsiteApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainWebsiteApp.urls')),
]
