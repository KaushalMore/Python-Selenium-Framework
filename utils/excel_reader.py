import os
import openpyxl


def get_test_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    file_path = os.path.join(base_path, "test_data", "login_credentials_sauce_demo.xlsx")

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook["Sheet1"]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if any(row):
            data.append(row)

    return data
