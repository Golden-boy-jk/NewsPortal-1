from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('home/', include('django.contrib.flatpages.urls')),
]


