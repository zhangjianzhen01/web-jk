from django.urls import path
from web.views import get_serial_numbers, New_order,get_id

urlpatterns = [
    path('api/cx/<str:materiel_pcode>/', get_serial_numbers),
    path('api/xz', New_order),
    path('api/cs', get_id),
    # 其他URL路由...
]