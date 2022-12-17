from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_info),
    # path('<int:id>', views.result_page, name='results')

]