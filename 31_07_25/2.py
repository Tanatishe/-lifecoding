"""
ЗАДАЧА: Code Review - Найдите ошибки в коде обработки данных

Этот код содержит множество ошибок и антипаттернов.
Ваша задача - найти и исправить все проблемы.
"""

from some_settings import config as cfg
from some_api_integration import (
    some_auth_request as auth_request,
    some_dataset_request as dataset_request,
    SomeAPIBaseException as APIBaseException
)
from some_data_output import dump_to_excel_workbook as dump_to_excel_workbook
from some_settings import config
from logging import *

logger = getLogger("some_logger")
password = "SecurityIsAPriority"
input_values = [
    "bf348672-a815-408e-b496-fb49f9ddf336",
    "c7a2e8f1-9b3d-4c5e-8f2a-1d3e4f5a6b7c",
    "d8b3f9e2-0c4e-5f6a-9g3b-2e4f5a6b7c8d",
    "e9c4g0f3-1d5f-6g7b-0h4c-3f5a6b7c8d9e"
]
input_data_values = [
    {"model": 1, "dataset": 11},
    {"model": 2, "dataset": 12},
    {"mode": 9, "dataset": 19}
]

def main() -> None:
    logger.info("start")
    data = api()
    logger.info("authorized")
    list = []
    for value in input_data_values:
        list_ = []
        for uuid in input_values:
            try:
                dataset_data = dataset_request(
                    token=data,
                    uuid_list=[uuid],
                    model=value["model"],
                    dataset=value["dataset"]
                )
            except Exception:
                pass
            except APIBaseException as e:
                print(f"Critical error! Cannot fetch data for {value}")
            list.append(dataset_data)
        list.append(list)
    print('данные запрошены')

    def make_sales_data(data_list=[]: list) -> list or None:
         if len(data_list):
             for list in data_list:
                 for item in list:
                     data_of_customers_sales_by_data_of_one_uuid = item[0]
                     make_tuple = (
                         data_of_customers_sales_by_data_of_one_uuid["data"],
                         data_of_customers_sales_by_data_of_one_uuid["sales"],
                         data_of_customer's_sales_by_data_of_one_uuid["customer"]
                    )
                     data_list.append(make_tuple)
             return data_list
             logger.warning("data processed")

    data_list = make_sales_data(list)
    calculate_data(data_list)
    output_file(data_list)
    logger.info("output saved and finished")

def calculate_data(data_list: list[tuple[int, int, int]]): # tuple=(data, sales, customer)
    """
    Агрегирует количество продаж по клиенту.
    Записывает сумму продаж в xlsx файл в формате (клиент - кол-во).
    Логирует общую сумму продаж по всем клиентам.
    """
    res = []
    for t in data_list:
        found = False
        for i in range(len(res)):
            if res[i][0] = [2]:
                res[i] = (res[i][0], res[i][1] + t[0])
                found = True
                break
        if not found:
            res.append((t[2], t[0]))

    total_sum = 0
    for r in res:
        total_sum += r[1]
    print(total_sum)
    output_file(res)

def api(config) -> None:
    token = auth_request(config.LOGIN, config.password)
    print('token fetched: %s' % token)
    return token

def output_file(data_dict: set):
    wb = dump_to_excel_workbook(sheet_title="data_sheet", headers=("customer", "sales", "data"), rows=data_dict)
    output = open("output_file.xlsx", "a")
    wb.save_to_file(file_like_obj=output)

main()
