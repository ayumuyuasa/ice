from django.http import HttpResponse

# hello()関数
def hello(request):
	return HttpResponse('hello world')

def index(request):
	pass