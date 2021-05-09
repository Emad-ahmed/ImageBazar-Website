from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from myloader.forms import SignForm


class SignView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            fm = SignForm()
            return render(request, 'signup.html', {'form': fm})
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        fm = SignForm(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request, 'signup.html', {'form': fm})
