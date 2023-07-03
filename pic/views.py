from django.http import request
from django.shortcuts import redirect, render
from .models import Picture

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView
)


def buyPicture(request,*args,**kwargs):
    picId = kwargs.get('pk')
    pic = Picture.objects.get(id = picId)
    user = request.user

    pic.user = user
    pic.save()
    return redirect('/')


def allPictures(request):

    context = {
        'pics': Picture.objects.all()

    }
    print(context)
    return render(request,'pic/pictures.html',context)


class PictureListView(ListView):

    model = Picture
    template_name = "pic/pictures.html"
    context_object_name = "pics"

class PictureDetailView(DeleteView):

    model = Picture
    template_name = "pic/picture_detail.html"

class PictureCreateView(LoginRequiredMixin,CreateView):

    model = Picture

    fields = ['name', 'image', 'price', 'discounts']

    def form_valid(self,form):

        form.instance.user = self.request.user
        return super().form_valid(form)

class PictureUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Picture

    fields = ['name', 'price', 'discounts']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        pic = self.get_object()

        if self.request.user == pic.user:
            return True
        return False

class PictureDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Picture
    success_url = "/"

    def test_func(self):
        pic = self.get_object()
        if self.request.user == pic.user:
            return True
        return False


        
        






