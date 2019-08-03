from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'index.html')
