from django.urls import path
from . import views
urlpatterns = [
    path("register/" , views.register_view , name="register" ),
    path("login/" , views.login_view , name="login" ),
    path("logout/" , views.logout_view , name="logout" ),
    path("update/" , views.updated_view , name="update" ),
    path("about/" , views.about_view , name="about" ),
]