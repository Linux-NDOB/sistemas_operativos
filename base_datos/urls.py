from django.urls import path
from .views import cpu_view, memory_view
app_name = "base_datos"

urlpatterns = [
    path("cpu/",cpu_view.as_view()),
    path("cpu/<int:pid>",cpu_view.as_view()),
    path("memory/", memory_view.as_view()),
    path("memory/<int:pid>", memory_view.as_view()),
]