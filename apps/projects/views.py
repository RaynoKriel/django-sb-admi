from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjectForm
from .models import projects
from django.contrib.auth.decorators import login_required

# Create your views here.


# method 1 (projects_create_view) fast and easy way to add a form to the app
#
@login_required(login_url='/accounts/login/')
def projects_create_view(request):
	form = ProjectForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProjectForm()
	context = {
            'form': form
	}
	return render(request, "projects/projects_create.html", context)


@login_required(login_url='/accounts/login/')
def projects_update_view(request, id=id):
	obj = get_object_or_404(projects, id=id)
	form = ProjectForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	#context['message'] = ' Details Updated. '
	return render(request, "projects/projects_create.html", context)


def projects_detail_view(request, id):
	obj = get_object_or_404(projects, id=id)
	# method 1 type out each column or variable you want to display by calling the object from the table
	#context = {
	#	'name': obj.name,
	#	'surname': obj.surname,
	#	'ign': obj.ign,
	#	'team': obj.team,
	#	'level': obj.level
	#}
	#or
	#method 2 you just add the object string infromt of all variables in the view
	context = {
            "object": obj
	}
	return render(request, "projects/projects_detail.html", context)


@login_required(login_url='/accounts/login/')
def projects_delete_view(request, id):
	obj = get_object_or_404(projects, id=id)
	#POST request
	if request.method == "POST":
	 	#confirming delete
		obj.delete()
		return redirect('../../')
	context = {
            'object': obj
	}
	return render(request, "projects/projects_delete.html", context)


def projects_list_view(request):
	queryset = projects.objects.all()  # list of objects
	context = {
		"object_list": queryset
	}
	return render(request, "projects/projects_list.html", context)


def dynamic_lookup_view(request, id):
	#obj = projects.objects.get(id=id)
	#obj = get_object_or_404 (projects, id=id)
	try:
		obj = projects.objects.get(id=id)
	except projects.DoesNotExist:
		raise Http404

	context = {
		"object": obj
	}
	return render(request, "projects/projects_detail.html", context)
