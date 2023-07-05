from django.urls import path
from cs.views import get_serial_numbers

urlpatterns = [
    path('api/cx/<str:materiel_pcode>/', get_serial_numbers),
    # 其他URL路由...
]
