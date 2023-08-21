from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sawo import createTemplate, getContext, verifyToken
from .models import Profile


class UserCreateView(SuccessMessageMixin,CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Your account was created successfully'
    


@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Account has been updated.')
            
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)
 
    return render(request, 'users/profile.html', {'uform': uform, 'pform': pform})



@login_required
def SearchView(request):
    if request.method == 'POST':
        kerko = request.POST.get('search')
        print(kerko)
        results = User.objects.filter(username__contains=kerko)
        context = {
            'results':results
        }
        return render(request, 'users/search_result.html', context)

from .models import Config
from sawo import getContext

def sawo_login(request):
    config = Config.objects.order_by('-api_key')[:1]
    context = {
        "sawo": getContext(config,"login") 
               
    }
    createTemplate("users/login.html")