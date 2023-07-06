from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from variable import public_variable

# 公共变量
tk = public_variable.APIHelper.tk
jk_url = public_variable.APIHelper.jk_url


# 查询序列号
@csrf_exempt
def get_serial_numbers(request, materiel_pcode):
    url = f'{jk_url}SerialStock?page=1&limit=50&materiel_pcode={materiel_pcode}&status=0'
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    response = requests.get(url, headers=headers)
    data = response.json()['data']
    qn_list = [item['qn'] for item in data]
    qn_string = '\n'.join(qn_list)

    return JsonResponse({'serialNumbers': qn_list})
