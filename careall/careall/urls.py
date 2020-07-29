"""careall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from accounts.views import index, thankyou, guest_thankyou

admin.site.site_header = "KareMe "
admin.site.site_title = "KareMe Admin Portal"
admin.site.index_title = "Welcome to KareMe Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('thankyou/', thankyou, name='thankyou'),
    path('guest-thankyou/', guest_thankyou, name='guest_thankyou'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('ratings/', include(('star_ratings.urls','ratings'), namespace='ratings')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
