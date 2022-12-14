from django.urls import path
from . import views

# app_name과 path 이름으로

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("<int:pk>/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.change_password, name="change_password"),
    path("delete/", views.delete, name="delete"),
   
    path("profile/update/", views.profile_update, name="profile_update"),
    path("<int:pk>/wishlist", views.wishlist, name="wishlist_list"),
    path('<int:pk>/follow/', views.follow, name='follow'),
    #path("profile/password/", views.password_edit_view, name="password_edit"),
]
