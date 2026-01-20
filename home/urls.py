
from django.urls import path

from . import views

urlpatterns = [

    path("",views.home, name="home"),
    path("Add_dare/",views.add_dare, name="add_dare"),
    path("my_dare/",views.dares, name="dares"),

    path("delete-dare/<int:id>",views.delete_dare,name="delete_dare"),

    path("edit_dare/<int:id>",views.edit_dare,name="edit_dare"),

    

]