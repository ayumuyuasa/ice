from django.db import models
from django.utils import timezone

class Maker(models.Model):
	maker_name = models.CharField('メーカー', max_length=255)
	created_at = models.DateTimeField('日付', default=timezone.now)

	def __str__(self):
		return self.maker_name

class Item(models.Model):
	ice_name = models.CharField('名称', max_length=255)
	description = models.TextField('説明', max_length=1000, null=True)
	price = models.CharField('価格', max_length=255)
	amount = models.CharField('内容量', max_length=255)
	image = models.CharField('商品画像', max_length=255)
	maker = models.ForeignKey(
		Maker, verbose_name='メーカー', on_delete=models.PROTECT,
		)
	created_at = models.DateTimeField('日付', default=timezone.now)

	def __str__(self):
		return self.ice_name

