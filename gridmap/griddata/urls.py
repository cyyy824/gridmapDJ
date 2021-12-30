from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gn/<int:gnid>', views.gridnode),
    path('esuport/<int:gnid>', views.edit_support),
    path('emembers/<int:gnid>', views.edit_member),
    path('dmember', views.del_member)
]