"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import  views as auth_views
from blog import views
from django.conf import settings
from django.conf.urls.static import static

#SOCIAL_AUTH_URL_NAMESPACE = 'social'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.index,name='index'),
    #path('datetime/',views.current_datetime,name='datetime'),
    path('',views.post_list,name='post_list'),
    path('blog/',include('blog.urls', namespace='blog')),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('register/',views.register,name='register'),

    # password reset
    #path('password-reset/',auth_views.PasswordResetView.as_view(),name= 'password_reset'),
    #path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    #path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/',include('social_django.urls', namespace='social')),
    path('likes/',views.like_post,name='like_post'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
