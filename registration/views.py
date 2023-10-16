from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse
from .forms import RegForm
from .models import Registration

def index(request):
    return render(request, 'Index.html')
    # return HttpResponse("<h2>Hello world2</h2> main")

def form(request):
    # form = RegForm()
    # print(dir(form))
    # context = {
    #     "form": form
    # }

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # fields = ["fio", "university", "tel", "email"]
            fio = form.cleaned_data["fio"]
            university= form.cleaned_data["university"]
            tel= form.cleaned_data["tel"]
            email= form.cleaned_data["email"]

            new_reg=form.save(commit=False)
            new_reg.save()

            # print(form.cleaned_data["fio"])



            # redirect to a new URL:
            return HttpResponseRedirect("/registration/")

        # if a GET (or any other method) we'll create a blank form
    else:
        form = RegForm()


    return render(request, 'Registration.html',{"form": form})
    # return HttpResponse("Hello world. Registration")

