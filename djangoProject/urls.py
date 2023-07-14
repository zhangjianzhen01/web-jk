from django.urls import path
from web.views import get_serial_numbers, New_order,huanbi, search, create

urlpatterns = [
    path('api/cx/<str:materiel_pcode>/', get_serial_numbers),
    path('api/xz', New_order),
    path('api/hb', huanbi),
    path('api/user', search),
    path('api/wo', create)
    # 其他URL路由...
]
