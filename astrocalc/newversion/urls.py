from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_info2, name='home'),
    path('about', views.about, name='about'),
    path('result/<int:main>/<int:matrix>/<int:num>', views.result),
]