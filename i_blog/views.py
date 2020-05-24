from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, Extra
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Company, Extra
from .forms import InfoCreateForm

# Create your views here.

class InfoListView(TemplateView):
    template_name = 'i_blog/home.html'


class InfoCreateView(CreateView):
    model = Company
    form_class = InfoCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.resume == '':
            form.instance.resume = self.request.user.profile.default_resume
        return super().form_valid(form)



class InfoUpdateView(UpdateView):
    model = Company
    fields = ['name', 'status', 'link', 'website', 'tagline', 'perks', 'skills', 'status']
    


class UserInfoListView(ListView):
    model = Company
    context_object_name = 'objects'
    paginate_by = 3
    # queryset = Company.objects.filter(user.username == 'encrypto')

    def get_queryset(self):
        user = get_object_or_404(User, username = self.request.user.username)
        return Company.objects.filter(user = user)






class InfoDetailView(DetailView):
    model = Company
    

