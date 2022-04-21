from django.urls import path
from blog import views

urlpatterns = [
    path("",views.ListBlogAPIView.as_view(),name="Blog_list"),
    path("create/", views.CreateBlogAPIView.as_view(),name="Blog_create"),
    path("update/<int:pk>/",views.UpdateBlogAPIView.as_view(),name="update_Blog"),
    path("delete/<int:pk>/",views.DeleteBlogAPIView.as_view(),name="delete_Blog")
]