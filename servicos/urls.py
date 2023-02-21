from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('addservico/', views.addServico, name="add-servico"),
    path('servico/<int:id>', views.servicoView, name='servico-view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/removeServico/<int:id>', views.removeServico, name='rm-servico'),
    path('dashboard/editServico/<int:id>', views.editServico, name='edit-servico'),
    path('help/', views.help, name='help')

] 