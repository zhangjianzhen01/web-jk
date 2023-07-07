from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests, datetime, random, json
from variable import public_variable

# 公共变量
tk = public_variable.APIHelper.tk
jk_url = public_variable.APIHelper.jk_url
null = None
false = False
true = True


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


# 新增销售订单、采购订单
@csrf_exempt
def New_order(request):
    # 定义逻辑
    # id={1；新建采购订单   2：新建采购资金平台订单   3：新建销售订单}
    # 获取当前年份
    current_year = datetime.datetime.now().year
    # 获取当前日期
    current_date = datetime.datetime.now().strftime('%m%d')
    # 生成一个随机的三位数
    random_number = random.randint(100, 999)
    random_number1 = random.randint(100, 999)
    # 生成采购订单代码
    purchase_order_code = f"CD{current_year}{current_date}{random_number}"
    # 生成浪潮订单代码
    voucher_abstract = f"SVL{current_year}{current_date}{random_number1}"
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        # 如果id=1，处理新建采购订单
        if id == 1:
            url = f'{jk_url}PurchaseOrderBase'
            headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
            data = {"invoice_company": "上海华胄网络科技有限公司", "invoice_type": 0,
                    "invoice_type_name": "增值税普通发票", "id": 0,
                    "handle_id": "", "sales_order_no": [], "sales_id": "", "purchase_type_name": "浪潮备货",
                    "purchase_type": "218", "platform_spot": "", "season_return": 0, "year_return": 0,
                    "quoted_price": "",
                    "million_return": 0, "promotion": "", "voucher_abstract": f"{voucher_abstract}",
                    "cancel_order_cost": "",
                    "lc_sale_id": "", "order_type_id": "", "industry_id": "", "fund_platform_id": "",
                    "purchase_order_date": "",
                    "original_order_amount": "80000", "lc_interest": "", "purchase_total_amount": 80000,
                    "no_tax_price": 70796.46, "fund_platform_interest": "", "promotion_source": "",
                    "is_direct_customer": 0,
                    "direct_customer_address": "", "remark": "", "purchase_order_code": f'{purchase_order_code}',
                    "supply_unit_id": 443,
                    "deliver_goods_date": "", "fund_platform_price": "", "rebate_rate1": "", "rebate_rate2": "",
                    "rebate_amount1": 0, "rebate_amount2": 0, "season_rebate_rate": "", "year_rebate_rate": "",
                    "million_rebate_rate": "", "is_return_amount": "", "return_amount": "", "fund_platform_amount": "",
                    "product_line_id": 39, "payment_amount": "", "not_payment_amount": 80000, "invoice_amount": "",
                    "not_invoice_amount": 80000, "term_days": "30"}
            response = requests.post(url=url, headers=headers, json=data)
            r = response.json()['message']
            if r == 'success':
                return JsonResponse({'message': '新建采购订单成功'})
            else:
                return JsonResponse({'message': '出错啦'})
        elif id == 2:
            # 如果id=2，处理新建资金平台采购订单
            url = f'{jk_url}PurchaseOrderBase'
            headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
            data = {"invoice_company": "上海华胄网络科技有限公司", "invoice_type": 0,
                    "invoice_type_name": "增值税普通发票", "id": 0, "handle_id": "", "sales_order_no": [],
                    "sales_id": "", "purchase_type_name": "浪潮备货", "purchase_type": "218", "platform_spot": "",
                    "season_return": 0, "year_return": 0, "quoted_price": "", "million_return": 0, "promotion": "",
                    "voucher_abstract": f"{voucher_abstract}", "cancel_order_cost": "", "lc_sale_id": "",
                    "order_type_id": 102,
                    "industry_id": "", "fund_platform_id": [4, 5], "purchase_order_date": "",
                    "original_order_amount": "9000", "lc_interest": "", "purchase_total_amount": 9000,
                    "no_tax_price": 7964.6, "fund_platform_interest": 1000, "promotion_source": "",
                    "is_direct_customer": 0, "direct_customer_address": "", "remark": "",
                    "purchase_order_code": f"{purchase_order_code}", "supply_unit_id": 224, "deliver_goods_date": "",
                    "fund_platform_price": "", "rebate_rate1": "", "rebate_rate2": "", "rebate_amount1": 0,
                    "rebate_amount2": 0, "season_rebate_rate": "", "year_rebate_rate": "", "million_rebate_rate": "",
                    "is_return_amount": "", "return_amount": "", "fund_platform_amount": "10000", "product_line_id": 39,
                    "payment_amount": "", "not_payment_amount": 9000, "invoice_amount": "", "not_invoice_amount": 9000,
                    "term_days": "30"}
            response = requests.post(url=url, headers=headers, json=data)
            r = response.json()['message']
            if r == 'success':
                return JsonResponse({'message': '新建采购资金平台订单成功'})
            else:
                return JsonResponse({'message': '出错啦'})
        elif id == 3:
            url = f'{jk_url}NuclearpriceBaojia'
            headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
            data = {"prepare_list": [], "company_address": "", "special_config_list": [], "special_list": [],
                    "borrow_list": [], "outside_list": [], "total_tax_cost": "0", "total_tax_removal_price": "",
                    "account_period_day": 20, "invoice_type": 1, "invoice_type_name": "N类（0%）(0%)",
                    "drawer_time": "2023-07-06T06:31:33.192Z", "type": 0, "period_list": [], "customer_id": 5053,
                    "allData": "", "id": 0, "drawer_name": "张健桢", "service_list": [], "baojia_name": "tets",
                    "customer_name": "测试客户", "baojia_list": [
                    {"id": 67, "np_product_code": "A0446", "handpiece_name": "（A0446）NF5270M5（标空）",
                     "handpiece_code": "A0446", "handpiece_type_id": 2, "old_handpiece_code": "", "weight": 3,
                     "describe": "CPU*0/内存*0/硬盘*0/背板*0/RAID*0/板载双口千兆/电源*0/电源线*0/导轨", "status": 1,
                     "attr": 1, "creator_id": 43, "created_at": "2022-04-22 08:49:34",
                     "updated_at": "2022-05-17 18:19:15", "deleted_at": 0, "children": [
                        {"id": 134, "np_product_code": "A0446", "np_product_quantity": 1, "handpiece_id": 67,
                         "created_at": "2022-05-16 14:41:23", "updated_at": "2022-05-16 14:41:23", "deleted_at": 0,
                         "np_product_price": "6200.00",
                         "np_product_name": "浪潮NF5270M5服务器（标空）CPU*0/内存*0/硬盘*0/背板*0/RAID*0/板载双口千兆/电源*0/导轨",
                         "type": 3, "source": false, "isHost": true, "unity_id": 2,
                         "np_product_price_total": "6200.00"},
                        {"np_product_id": 1678, "np_product_code": "B0079", "np_old_product_code": null,
                         "np_product_name": "浪潮 CPU散热器 for 2U M5机架式", "np_product_pmodule": null,
                         "np_buy_code": null, "np_product_line": 0, "np_product_line_name": null, "np_suppliers": 0,
                         "np_suppliers_name": null, "np_lc_attr": 0, "np_lc_attr_name": null, "np_bar_code": null,
                         "np_unit": 0, "np_unit_name": null, "np_product_type": "C", "np_product_price": "200.00",
                         "np_integral": 0, "np_cost_price_a": "160.00", "np_product_alias_name": "M5散热器2U",
                         "np_img_src": null, "np_slider_image": null, "np_description": null, "np_volume": "0.00",
                         "np_weight": null, "np_cate": "0", "np_cate_level": 1, "status": 1,
                         "classify_id": ["238", "274"], "cate_id": 274, "np_explain": null, "np_remark": null,
                         "PCode": "B0079", "np_tag": [36], "unit": "件", "new_np_tag": null, "creator_id": 42,
                         "created_at": "2022-06-16 11:23:11", "updated_at": "2023-06-26 18:00:13", "deleted_at": 0,
                         "host_type": null, "weight": 0, "tax_rate": null, "tax_amount": null, "no_tax_price": null,
                         "stock_num": 299, "is_sup": 0, "is_np": 0, "is_kpi": 0, "is_gift": null, "system": null,
                         "cate_name": "散热器", "id": 1688625120000, "TagList": ["2U散热器（M5）"], "source": "hejia",
                         "np_product_quantity": 1, "type": 2, "isHost": true, "unity_id": 3,
                         "np_product_price_total": "200.00"}], "np_product_name": "（A0446）NF5270M5（标空）",
                     "np_product_quantity": 1, "type": 1, "new_source": 1, "tax_rate": 0, "total_amount": 10000,
                     "unity_id": 1, "np_product_price_total": "6400.00", "np_product_price": "6400.00",
                     "np_sales_quantity": 10000, "tax_removal_price": "10000.00", "tax_cost": "0.00"}],
                    "customer_contact": "测试", "customer_phone": "15288888888", "customer_fax": null,
                    "location": [1, 2, 3], "customer_address": " 山海关区", "pay_condition": 1, "pay_remark": null,
                    "company_province": 1, "company_city": 2, "company_area": 3, "reference_price": 6400,
                    "sales_price": 10000, "customer_province": 1, "customer_city": 2, "customer_area": 3}
            response = requests.post(url=url, headers=headers, json=data)
            baojia = response.json()['data']

            bj_url = f'{jk_url}NuclearpriceBaojiaReview/{baojia}'
            bj_headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
            response = requests.get(url=bj_url, headers=bj_headers)
            bjd_url = f'{jk_url}NuclearpriceBaojiaDetail/{baojia}'
            bjd_headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
            response = requests.get(url=bjd_url, headers=bjd_headers)
            baojia_no = response.json()['data']['baojia_no']

            xs_url = f'{jk_url}SalesOrder'
            xs_headers = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
            xs_data = {"baojia_id": f'{baojia}', "business_info": {"business_category": ""}, "business_id": 0,
                       "ext_info": {"location": [], "serve_customer_id": "1", "serve_customer_name": "公司",
                                    "serve_customer_contact": "11", "serve_customer_phone": "112233344",
                                    "serve_customer_province": "2", "serve_customer_city": "2",
                                    "serve_customer_area": "3", "serve_customer_address": "xxxxx"},
                       "alter_order_list": [], "is_batches": 0, "location": [1, 2, 3], "status": 0,
                       "borrow_order_id": f'{baojia}', "drawer_time": "2023-07-06", "sales_amount": "10000.00",
                       "out_type": "",
                       "sales_man": "张健桢", "sales_dept": "魔鸽数据", "abstract": "", "request_type": 1,
                       "invoice_company": "上海华胄网络科技有限公司", "kp_business_no": "", "order_list": [
                    {"id": 33361, "baojia_id": f'{baojia}', "change_order_id": 0, "purchase_order_detail_id": null,
                     "purchase_order_code": null, "parent_id": 0, "np_product_code": "A0446",
                     "np_product_name": "（A0446）NF5270M5（标空）", "np_product_price": "6400.00",
                     "np_sales_quantity": "10000.00", "examine_price": "0.00", "cost_examine_price": "0.00",
                     "np_product_quantity": 1, "verify_quantity": null, "tax_rate": "0",
                     "tax_removal_price": "10000.00", "tax_cost": "0.00", "remark": null, "type": 1, "item_source": 1,
                     "new_source": 1, "change_type": null, "total_amount": "10000.00", "relation_id": 0,
                     "creator_id": 113, "unity_id": "1", "stock_num": "0", "cate_id": 395,
                     "cate_name": {"id": 395, "name": "NF5270M5", "code": "", "mcode": "", "parent_id": 237,
                                   "weight": 6, "operator_id": 1, "created_at": "2022-12-14 15:12:24",
                                   "updated_at": "2022-12-15 21:49:38", "deleted_at": 0, "operator_name": "Admin",
                                   "isRootInsert": false, "elm": {}}, "PCode": "A0446",
                     "np_product_alias_name": "NF5270M5（标空）", "np_old_product_code": null,
                     "NuclearpriceHandpieceInfo": {"id": 67, "np_product_code": null,
                                                   "handpiece_name": "（A0446）NF5270M5（标空）", "handpiece_code": "A0446",
                                                   "handpiece_type_id": 2, "old_handpiece_code": "", "weight": 3,
                                                   "describe": "CPU*0/内存*0/硬盘*0/背板*0/RAID*0/板载双口千兆/电源*0/电源线*0/导轨",
                                                   "status": 1, "attr": 1, "creator_id": 43,
                                                   "created_at": "2022-04-22 08:49:34",
                                                   "updated_at": "2022-05-17 18:19:15", "deleted_at": 0},
                     "DemandInfo": null, "children": [
                        {"id": 33362, "baojia_id": f'{baojia}', "change_order_id": 0, "purchase_order_detail_id": null,
                         "purchase_order_code": null, "parent_id": 33361, "np_product_code": "A0446",
                         "np_product_name": "浪潮NF5270M5服务器（标空）CPU*0/内存*0/硬盘*0/背板*0/RAID*0/板载双口千兆/电源*0/导轨",
                         "np_product_price": "6200.00", "np_sales_quantity": "0.00", "examine_price": "0.00",
                         "cost_examine_price": "0.00", "np_product_quantity": 1, "verify_quantity": null,
                         "tax_rate": null, "tax_removal_price": "0.00", "tax_cost": null, "remark": null, "type": 3,
                         "item_source": 1, "new_source": 1, "change_type": null, "total_amount": "0.00",
                         "relation_id": 0, "creator_id": 113, "unity_id": "2", "stock_num": "0", "cate_id": 395,
                         "cate_name": "NF5270M5", "PCode": "A0446", "np_product_alias_name": "NF5270M5（标空）",
                         "np_old_product_code": null, "NuclearpriceHandpieceInfo": {"id": 67, "np_product_code": null,
                                                                                    "handpiece_name": "（A0446）NF5270M5（标空）",
                                                                                    "handpiece_code": "A0446",
                                                                                    "handpiece_type_id": 2,
                                                                                    "old_handpiece_code": "",
                                                                                    "weight": 3,
                                                                                    "describe": "CPU*0/内存*0/硬盘*0/背板*0/RAID*0/板载双口千兆/电源*0/电源线*0/导轨",
                                                                                    "status": 1, "attr": 1,
                                                                                    "creator_id": 43,
                                                                                    "created_at": "2022-04-22 08:49:34",
                                                                                    "updated_at": "2022-05-17 18:19:15",
                                                                                    "deleted_at": 0},
                         "DemandInfo": null, "np_sales_price": "0.00"},
                        {"id": 33363, "baojia_id": f'{baojia}', "change_order_id": 0, "purchase_order_detail_id": null,
                         "purchase_order_code": null, "parent_id": 33361, "np_product_code": "B0079",
                         "np_product_name": "浪潮 CPU散热器 for 2U M5机架式", "np_product_price": "200.00",
                         "np_sales_quantity": "0.00", "examine_price": "0.00", "cost_examine_price": "0.00",
                         "np_product_quantity": 1, "verify_quantity": null, "tax_rate": null,
                         "tax_removal_price": "0.00", "tax_cost": null, "remark": null, "type": 2, "item_source": 1,
                         "new_source": 1, "change_type": null, "total_amount": "0.00", "relation_id": 0,
                         "creator_id": 113, "unity_id": "3", "stock_num": "299", "cate_id": 274,
                         "cate_name": {"id": 274, "name": "散热器", "code": "002", "mcode": null, "parent_id": 238,
                                       "weight": 2, "operator_id": 1, "created_at": "2022-06-30 11:12:11",
                                       "updated_at": "2022-12-14 11:13:32", "deleted_at": 0, "operator_name": "Admin",
                                       "isRootInsert": false, "elm": {}}, "PCode": "B0079",
                         "np_product_alias_name": "M5散热器2U", "np_old_product_code": null,
                         "NuclearpriceHandpieceInfo": null, "DemandInfo": null, "np_sales_price": "0.00"}],
                     "np_sales_price": "10000.00"}], "branch": 249, "invoice_type": 1,
                       "invoice_type_name": "增值税专用发票", "delivery_time": "2023-08-30", "business_pattern": 238,
                       "collected_method": "", "remark": "", "collection_period": "2023-08-30", "sales_type": 229,
                       "customer_id": 5053, "customer_name": "测试客户", "customer_contact": "测试",
                       "customer_phone": "15288888888", "customer_province": 1, "customer_city": 2, "customer_area": 3,
                       "customer_address": " 山海关区", "baojia_no": f'{baojia_no}'}
            response = requests.post(url=xs_url, headers=xs_headers, json=xs_data)
            # 将set类型转换为list类型
            xs_data["location"] = list(xs_data["location"])

            # 编码为JSON格式
            json_data = json.dumps(xs_data)
            order_id = response.json()['message']
            if order_id == 'success':
                return JsonResponse({'message': '新建销售订单成功'})
            else:
                return JsonResponse({'message': '出错啦'})
        return JsonResponse({'message': '操作未定义'})

    else:
        return JsonResponse({'message': '请求方式错误'})


# 获取token
@csrf_exempt
def get_id(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        return JsonResponse({'id': id})


# 环比增长计算
@csrf_exempt
def huanbi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        response = []

        for item in data['items']:
            q1 = float(item.get('q1', 0))
            q2 = float(item.get('q2', 0))

            if q1 == 0:
                response.append({'error': f'除数不能为零'})
            else:
                c = ((q2 - q1) / q1)
                result = round(c * 100, 2)
                response.append({'result': f'{result}%'})

        return JsonResponse({'results': response})
    else:
        return JsonResponse({'results': '请求方式错误'})