from django.urls import path
from . import views

urlpatterns = [
    path('insert_sow/', views.insert_sow, name="insert_sow"),
    path('fetch_sow/', views.fetch_sow, name="fetch_sow"),
    path('save_new_sow/', views.save_new_sow, name="save_new_sow"),
    path('generate_pdf/', views.generate_pdf, name="generate_pdf"),
    path('save_lesson/', views.save_lesson, name="save_lesson"),
    path('load_lesson/', views.load_lesson, name="load_lesson"),
    path('insert_load_lesson/', views.insert_load_lesson, name="insert_load_lesson"),
    path('delete_lesson/', views.delete_lesson, name="delete_lesson"),
    path('login_page/', views.login_page, name="login_page"),
    path('register_page/', views.register_page, name="register_page"),
    path('first_login/', views.first_login, name="first_login"),
    path('logout_page/', views.logout_page, name="logout_page"),
]