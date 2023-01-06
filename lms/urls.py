from django import template
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('', views.index,name='index'),
    path('books', views.books,name='books'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutuser,name='logout'),

    path('password_reset', auth_views.PasswordResetView.as_view(template_name='pages/Reset_password/password_reset.html'),name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='pages/Reset_password/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
     
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




