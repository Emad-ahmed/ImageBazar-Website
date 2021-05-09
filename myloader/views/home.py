from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from myloader.models import MyImage, Category
from myloader.forms import ShowImage


class HomeView(View):
    def get(self, request):
        mycategory = Category.objects.all()
        allimage = MyImage.objects.all()
        return render(request, 'home.html', {'allimage': allimage, 'cats': mycategory})

    def post(self, request):
        search = request.POST.get('search')
        mycategory = Category.objects.all()
        allimage = MyImage.objects.filter(name=search)
        return render(request, 'home.html', {'allimage': allimage, 'cats': mycategory})


def showcat(request, id):
    if request.method == "POST":
        search = request.POST.get('search')
        mycategory = Category.objects.all()
        allimage = MyImage.objects.filter(name=search)
        return render(request, 'home.html', {'allimage': allimage, 'cats': mycategory})

    mycategory = Category.objects.all()
    category = Category.objects.get(pk=id)
    allimage = MyImage.objects.filter(cat=category)
    return render(request, 'home.html', {'allimage': allimage, 'cats': mycategory})


def addphoto(request):
    if request.user.is_superuser:
        if request.method == "POST":
            fm = ShowImage(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
        else:
            fm = ShowImage()
            return render(request, 'addimage.html', {'form': fm})

        return render(request, 'addimage.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')
