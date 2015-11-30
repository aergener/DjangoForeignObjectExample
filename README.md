python 2.7.10

pip install -r requirements.txt

django-admin startproject foreignobject

django-admin startapp app

add 'app' to settings installed apps
& 'rest_framework'

create models

makemigrations
migrate

create some stuff
python manage.py shell
"""
stock_name = 'Ergicorp'
stock_id = 12345
dateval0 = '2014-11-10'
dateval1 = '2015-11-10'

Stock.objects.create(stock_id=stock_id, dateval=dateval0, stock_name=stock_name)
Stock.objects.create(stock_id=stock_id, dateval=dateval1, stock_name=stock_name)
map(lambda x: (x.dateval, x.stock_id, x.stock_name), Stock.objects.all())

Price.objects.create(stock_id=stock_id, dateval=dateval0, price=100.0)
Price.objects.create(stock_id=stock_id, dateval=dateval1, price=110.0)
map(lambda x: (x.dateval, x.stock_id, x.price), Price.objects.all())

stock = Stock.objects.get(stock_id=12345, dateval='2015-11-10')
stock.price.price

price = Price.objects.get(stock_id=12345, dateval='2015-11-10')
price.stock.stock_name
"""

create serializers
create views

add urls
