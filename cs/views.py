from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests


@csrf_exempt
def get_serial_numbers(request, materiel_pcode):
    url = f'http://192.168.0.21:9090/SerialStock?page=1&limit=50&materiel_pcode={materiel_pcode}&status=0'
    tk = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbl9pZCI6MTEzLCJhdWQiOiIiLCJleHAiOjE3MTQyNzAzNjksImlhdCI6MTY4ODM1MDM2OSwiaXNzIjoiIiwianRpIjoiZWU4MjhjNDYzN2Q2YTBhY2VjNTY0ODZkMTI2YjJmNWYiLCJuYmYiOjE2ODgzNTAzNjksInN1YiI6IiJ9.GGNRm3H7lw9VJzj7uzgqsEq4fF5vtzdObWJG_-1bNks'  # 替换为您的token
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    response = requests.get(url, headers=headers)
    data = response.json()['data']
    qn_list = [item['qn'] for item in data]
    qn_string = '\n'.join(qn_list)

    return JsonResponse({'serialNumbers': qn_list})
