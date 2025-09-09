from blog.views import show_all_post , post_details , create_post , delete_post , home_page
from django.urls import path

urlpatterns = [
    path("", show_all_post, name="show_post"),
    path("posts/<int:pr>/", post_details, name="post_details"),
    path("posts/create/", create_post, name="create_post"),
    path("posts/<int:pr>/delete", delete_post, name="delete_post"),
    path("posts/home/" , home_page , name="home_page")

   
]
