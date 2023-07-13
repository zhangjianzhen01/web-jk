from django.urls import path
from web.views import get_serial_numbers, New_order,get_id,huanbi,search

urlpatterns = [
    path('api/cx/<str:materiel_pcode>/', get_serial_numbers),
    path('api/xz', New_order),
    path('api/cx', get_id),
    path('api/hb', huanbi),
    path('api/user', search)
    # 其他URL路由...
]