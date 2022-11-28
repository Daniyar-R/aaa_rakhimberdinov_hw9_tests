from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest


def test_format_1():
    """ Проверка формата даты YYYY-MM-DD """
    with patch('urllib.request.urlopen') as mocked_get_cases_1:
        with patch('json.load') as mocked_get_cases_2:
            mocked_get_cases_2.return_value = \
                {'currentDateTime': '2022-11-24 00:00:00'}
            assert what_is_year_now() == 2022
            mocked_get_cases_1.assert_called_once()


def test_format_2():
    """ Проверка формата даты DD.MM.YYYY """
    with patch('urllib.request.urlopen') as mocked_get_cases_1:
        with patch('json.load') as mocked_get_cases_2:
            mocked_get_cases_2.return_value = \
                {'currentDateTime': '07.08.2023 12:12:12'}
            assert what_is_year_now() == 2023
            mocked_get_cases_1.assert_called_once()


def test_format_3():
    """ Проверка неправильного формата даты YYYY.MM.DD """
    with patch('urllib.request.urlopen') as mocked_get_cases_1:
        with patch('json.load') as mocked_get_cases_2:
            mocked_get_cases_2.return_value = \
                {'currentDateTime': '2022.11.24 00:00:00'}
            assert what_is_year_now() == 2022
            mocked_get_cases_1.assert_called_once()


def test_raise_type_error():
    """ Проверка получения ошибки"""
    with patch('urllib.request.urlopen') as mocked_get_cases_1:
        with patch('json.load') as mocked_get_cases_2:
            with pytest.raises(ValueError):
                what_is_year_now()
