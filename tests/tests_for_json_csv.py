# -*- coding: utf-8 -*-
# @Time    : 29.06.2021 18:50
# @Author  : Marcin Lisiecki
# @FileName: tests_for_json_csv.py.py
# @Software: PyCharm
from jsonify_csvfy.json_csv import JsonToCSV
from tests.const_for_tests import FILE_PATH_JSON


def test_get_dict_from_json():
    output_dict = JsonToCSV.get_dict_from_json(FILE_PATH_JSON)
    assert output_dict == {'random': 6, 'random float': 42.971, 'bool': False, 'date': '1994-02-28',
                           'regEx': 'helloooooooooooooooooooooooooooooo to you', 'enum': 'generator',
                           'firstname': 'Leona', 'lastname': 'Gherardo', 'city': 'Vancouver', 'country': 'Tajikistan',
                           'countryCode': 'GF', 'email uses current data': 'Leona.Gherardo@gmail.com',
                           'email from expression': 'Leona.Gherardo@yopmail.com'}


def test_get_content():
    output_header, output_body = JsonToCSV.get_content()
    assert output_header == ['random', 'random float', 'bool', 'date', 'regEx', 'enum', 'firstname', 'lastname', 'city',
                             'country', 'countryCode', 'email uses current data', 'email from expression']
    assert output_body == [6, 42.971, False, '1994-02-28', 'helloooooooooooooooooooooooooooooo to you', 'generator',
                           'Leona', 'Gherardo', 'Vancouver', 'Tajikistan', 'GF', 'Leona.Gherardo@gmail.com',
                           'Leona.Gherardo@yopmail.com']
