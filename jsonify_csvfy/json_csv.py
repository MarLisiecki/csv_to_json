# -*- coding: utf-8 -*-
# @Time    : 28.06.2021 19:17
# @Author  : Marcin Lisiecki
# @FileName: json_csv.py.py
# @Software: PyCharm
import csv
import json

from tests.const_for_tests import FILE_PATH_JSON


class JsonToCSV:
    _dict_from_json = dict()

    @staticmethod
    def convert_json_to_csv():
        header_list, content = JsonToCSV.get_content()
        with open('../doc_for_tests/test_file_output_json.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header_list)
            writer.writerow(content)

    @staticmethod
    def get_content():
        dict_with_content = JsonToCSV.get_dict_from_json(FILE_PATH_JSON)
        header_list = list(dict_with_content.keys())
        body = list(dict_with_content.values())
        return header_list, body

    @staticmethod
    def get_dict_from_json(file_path):
        _dict_from_json = dict()
        with open(file_path) as json_file:
            _dict_from_json = json.load(json_file)
        return _dict_from_json


if __name__ == "__main__":
    # print(JsonToCSV.get_dict_from_json(FILE_PATH_JSON))
    content = JsonToCSV.get_content()
    for i in content:
        print(i)
