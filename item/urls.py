# url()関数のインポート
from django.urls import path
from . import views

app_name = 'item'

# ルーティングの設定
urlpatterns = [
	path('', views.hello, name='hello'),
]