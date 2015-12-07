from django.db import models

class ForeignObject(models.fields.related.ForeignObject):
    requires_unique_target = False

class Stock(models.Model):
    stock_id = models.IntegerField()
    dateval = models.DateField()
    stock_name = models.CharField(max_length=255)

    price = ForeignObject('Price',
                          from_fields=('stock_id','dateval',),
                          to_fields=('stock_id','dateval',),
                          related_name='stock_list',
                          unique=True)

    class Meta:
        unique_together = (('stock_id', 'dateval', ),)

class Price(models.Model):
    stock_id = models.IntegerField()
    dateval = models.DateField()
    price = models.FloatField()

    stock = ForeignObject('Stock',
                          from_fields=('stock_id','dateval',),
                          to_fields=('stock_id','dateval',),
                          related_name='price_list',
                          unique=True)

    class Meta:
        unique_together = (('stock_id', 'dateval', ),)
