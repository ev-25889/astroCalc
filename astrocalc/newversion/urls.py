from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_info2, name='home'),
    path('about', views.about, name='about'),
    path('result/<int:main>/<int:matrix>/<int:num>', views.result),
    # path('result/2/<int:matrix>/<int:num>', views.result2),
    # path('result/3/<int:matrix>/<int:num>', views.result3),
    # path('result/4/<int:matrix>/<int:num>', views.result4),
    # path('result/5/<int:matrix>/<int:num>', views.result5),
    # path('result/6/<int:matrix>/<int:num>', views.result6),
    # path('result/7/<int:matrix>/<int:num>', views.result7),
    # path('result/8/<int:matrix>/<int:num>', views.result8),
    # path('result/9', views.result9),
    # path('result/10', views.result10),
    # path('result/11', views.result11),
    # path('result/12', views.result12),
    # path('result/13', views.result13),
    # path('result/14', views.result14),
    # path('result/15', views.result15),
    # path('result/16', views.result16),
    # path('result/17', views.result17),
    # path('result/18', views.result18),
    # path('result/19', views.result19),
    # path('result/20', views.result20),
    # path('result/21', views.result21),
    # path('result/22', views.result22),

]