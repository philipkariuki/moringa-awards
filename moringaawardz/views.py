from django.shortcuts import render,redirect
from .models import Project, Profile, Comments
from .forms import CommentForm, ProfileUpdateForm, NewProjectForm
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
	allprojects = Project.get_projects()
	return render(request, 'project.html', {'project': allprojects})


@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})





def profile(request):
	try:
		profile =Profile.objects.get(name_id=request.user.id)
	except ObjectDoesNotExist:
		raise Http404()
	return render(request,'profile.html',{ 'profile':profile })



@login_required(login_url='/accounts/login/')
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileUpdateForm()
    return render(request, 'profile_update.html', {"form": form})






def new_comment(request):

	current_user = request.user

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = current_user
			profile.save()
		return HttpResponseRedirect('/')
	else:
		form = CommentForm()
	return render(request, 'new_comment.html', {"form": form})




def search_results(request):

    if 'projectsearch' in request.GET and request.GET["projectsearch"]:
        search_term = request.GET.get("projectsearch")
        searched_projects = Image.search_by_title(search_term)
        message = f"{search_term}"
        proj = Project.get_projects()

        return render(request, 'search.html',{"message":message,"projess": searched_projects, "prjz": proj})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})





@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('index')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})



