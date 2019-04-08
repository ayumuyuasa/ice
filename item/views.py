from django.views import generic

class IndexView(generic.TemplateView):
	template_name = 'item/item_list.html'