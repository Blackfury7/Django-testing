from django.shortcuts import (get_object_or_404,
							  render,
							  HttpResponseRedirect)

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm


def create_view(request):

	context ={}
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/")
		
	context['form']= form
	return render(request, "create_view.html", context)

# update view for details
def update_view(request, id):
	context ={}
  
	# fetch the object related to passed id
	obj = get_object_or_404(GeeksModel, id = id)
  
	# pass the object as instance in form
	form = GeeksForm(request.POST or None, instance = obj)
  
	# save the data from the form and
	# redirect to detail_view
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)
  
	# add form dictionary to context
	context["form"] = form
  
	return render(request, "update_view.html", context)


def list_view(request):
	context ={}
	context["dataset"] = GeeksModel.objects.all()
		  
	return render(request, "list_view.html", context)


# pass id attribute from urls
def detail_view(request, id):
	context ={}
  
	# add the dictionary during initialization
	context["data"] = GeeksModel.objects.get(id = id)
		  
	return render(request, "detail_view.html", context)

  
def delete_view(request, id):
	context ={}
  
	# fetch the object related to passed id
	obj = get_object_or_404(GeeksModel, id = id)
  
  
	if request.method =="POST":
		# delete object
		obj.delete()
		# after deleting redirect to 
		# home page
		return HttpResponseRedirect("/")
  
	return render(request, "delete_view.html", context)




