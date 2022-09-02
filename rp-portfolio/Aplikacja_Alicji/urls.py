from django.urls import path
from . import views

app_name = "Aplikacja_Alicji"
#{% url 'Aplikacja_Alicji:my_url_Aplikacja_Alicji' %}

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]