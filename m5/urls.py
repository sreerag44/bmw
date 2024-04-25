from django.urls import path
from . import views

urlpatterns = [

    path("",views.index),
    path("adminlogin/",views.adminloging),
    path("checklogin/",views.checklogin),
    path("homepage/",views.homepage),
    path("about/",views.about),
    path("service/",views.service),
    path("contact/",views.contact),
    path("service_view/",views.service_view),
    path("add_service/",views.add_service),
    path("saveservice/",views.saveservice),
    path("editdetails/<id>",views.editdetails),
    path("updatedetails/<id>",views.updatedetails),
    path("deletedetails/<id>", views.deletedetails),
    path("tech_view/",views.tech_view),
    path("savetech/",views.savetech),
    path("add_tech/",views.add_tech),
    path("edittech/<id>",views.edittech),
    path("updatetech/<id>",views.updatetech),
    path("deletetech/<id>",views.deletetech),
    path("booknow/<id>",views.booknow),
    path("savebooking/<id>",views.savebooking),
    path("paymentform/<id>",views.paymentform,name="paymentform"),
    path("index/",views.index)





]