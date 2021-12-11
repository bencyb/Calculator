
# from django.urls import path
# from . import views
# from thisapp import urls

# urlpatterns = [
#     path('',views.calc,name='calc')
# ]

from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('',views.index, name='calculator'),
    path('add',views.addition, name='add'),
    path('sub',views.subtraction, name='sub'),
    path('multi',views.multiplication, name='multi'),
    path('div',views.division, name='div')
]