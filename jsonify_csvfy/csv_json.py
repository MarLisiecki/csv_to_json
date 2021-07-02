# -*- coding: utf-8 -*-
# @Time    : 28.06.2021 19:18
# @Author  : Marcin Lisiecki
# @FileName: csv_json.py.py
# @Software: PyCharm
import csv
import json


class CSVToJson:

    @staticmethod
    def convert_csv_to_json():
        dict_from_csv = CSVToJson.convert_lists_to_dict()
        with open('../doc_for_tests/test_file_output.json', 'w') as jsonfile:
            json.dump(dict_from_csv, jsonfile)

    @staticmethod
    def get_lists_from_csv():
        body = list()
        with open('../doc_for_tests/test_file_output_json.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for index, row in enumerate(reader):
                if index == 0:
                    header = row
                elif row != []:
                    body.append(row)
            return header, body

    @staticmethod
    def convert_lists_to_dict():
        dict_from_csv = dict()
        row_number = 0
        header, body = CSVToJson.get_lists_from_csv()
        for index, element in enumerate(header):
            dict_from_csv[element] = body[row_number][index]

        return dict_from_csv


if __name__ == '__main__':
    pass
