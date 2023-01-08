from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('create-database/', views.create_db, name='create_db'),
    path('create-database/create-database-record', views.create_db_record, name='create_db_record'),
    path('show-databases/', views.show_dbs, name='show_dbs'),
    path('show-databases/<int:db_id>/show-passwords/', views.show_passwords, name='show_passwords'),
    path('show-databases/<int:db_id>/update-db', views.update_db, name='update_db'),
    path('show-databases/<int:db_id>/update-db/update-db-record', views.update_db_record, name='update_db_record'),
    path('show-databases/<int:db_id>/delete-db', views.delete_db, name='delete_db'),
    path('show-databases/<int:db_id>/delete-db/delete-db-record', views.delete_db_record, name='delete_db_record'),
    path('show-databases/<int:db_id>/show-passwords/create-new-password', views.create_pw, name='create_pw'),
    path('show-databases/<int:db_id>/show-passwords/create-new-password/create-pw-record', views.create_pw_record, name='create_pw_record'),
    path('show-databases/<int:db_id>/show-passwords/update-password/<int:pw_id>', views.update_pw, name='update_pw'),
    path('show-databases/<int:db_id>/show-passwords/update-password/update-pw-record/<int:pw_id>', views.update_pw_record, name='update_pw_record'),
    path('show-databases/<int:db_id>/show-passwords/delete-password/<int:pw_id>', views.delete_pw, name='delete_pw'),
    path('show-databases/<int:db_id>/show-passwords/delete-password/delete-pw-record/<int:pw_id>', views.delete_pw_record, name='delete_pw_record'),
]