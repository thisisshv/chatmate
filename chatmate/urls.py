from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('core.urls')),
    path('account/', include('users.urls')),
    path('chat/', include('chatroom.urls')),
]
