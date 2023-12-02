from django.contrib import admin
from django.urls import path,include
from mainapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'purchase',PurchaseViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('view_bill/<int:user_id>/',view_bill,name='view_bill'),
    path('Send_mail/',Send_mail,name="Send_mail"),
    path('api/',include(router.urls)),
]
