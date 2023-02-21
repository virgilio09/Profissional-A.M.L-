from django.contrib import auth
from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.UserCreationForm.as_view(), name='register'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('edit_profile/editSuccss/', views.editSuccess, name='edit_success'),
    path('password/', views.PasswordChangeView.as_view(), name='change_password'),
    path('password/passwordSuccess/', views.passwordSuccess, name='password_success'),
    path('my_account/', views.myAccount, name='my_account'),
    path('remove_user/', views.removeUser, name='remove_user')
   
]