from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # 根路徑對應部落格首頁
    path("about/", views.about, name="about"),  # /about/ 對應部落格關於頁面
]
