# API для работы с порталом https://newlk.erconline.ru/ (Мой Дом)
###### Установка 
`pip install moydomjkh`
###### Доступные функции: 
* Авторизация на портле 
* Получение базовой информации клиента с портала, которая нужна для последующих вызовов
* Получение списка переданных ранее показаний
* Получение списка оплат
* Передача показаний за текущий месяц

###### Режим CLI:
```
> moydomjkh -h
usage: moydomjkh [-h] -l LOGIN -p PASSWORD [-i] [-u] [-m METER]
                       [-r RESULT] [-v]

Please specify input parameters

optional arguments:
  -h, --help            show this help message and exit
  -l LOGIN, --login LOGIN
                        User login
  -p PASSWORD, --password PASSWORD
                        User password
  -i, --info            User account(s) information
  -u, --upload          Submit measurement
  -m METER, --meter METER
                        Meter id (required for upload)
  -r RESULT, --result RESULT
                        Measurement result (required for upload)
  -v, --verbose         Verbosity level (up to vvvvv)

```

Загрузка данных с портала
```
> moydomjkh -i -l **** -p *****
```
Получение данных в виде json либо сообщение об ошибке (при этом выполнение приложения завершается с статусом 1)

Загрукза данных на портал
```
> moydomjkh -u -l ***** -p **** -m *****-***-** -r *
```

Сделано по аналогии с https://github.com/kkuryshev/mosenergosbyt/