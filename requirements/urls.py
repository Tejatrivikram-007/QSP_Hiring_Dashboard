from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('add_requirement/',views.add_requirement,name='add_requirement'), 
    path('update_requirement/<int:id>/',views.update_requirement,name='update_requirement'),
    path('delete_requirement/<int:id>/',views.delete_requirement,name='delete_requirement'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
     path('reset_password/',views.reset_password_view,name='reset_password'),
    path('logout/', views.logout_view, name='logout'),

]