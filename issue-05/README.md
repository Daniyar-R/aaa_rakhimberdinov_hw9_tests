**README**

1. Сперва необходимо установить пакет:
> $ pip install pytest-cov
2. Войдем в папку issue-05 
> $ cd issue-05
3. Запустим тест в терминале
> $ python -m pytest -q issue_5.py --cov=what_is_year_now 
4. Сохраним отчет в html
> $ python -m pytest -q issue_5.py --cov=what_is_year_now --cov-report html
