from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('url address', 'view')
    path('', index_view),
    path('contacts', contacts_view),
    path('about', about_view)
]
