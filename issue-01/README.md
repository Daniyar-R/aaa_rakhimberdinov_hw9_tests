**README**


1. Для того чтобы сохранить результат в файле output запускаем в терминале:
> $ python -m doctest issue-01/*.py > issue-01/result
2. Чтобы запустить тесты с флагом NORMALIZE_WHITESPACE, 
который позволяет не различать последовательности пробелов и переносов строк:
> $ python -m doctest -o NORMALIZE_WHITESPACE -v issue-01/*.py > issue-01/result_whitespace
