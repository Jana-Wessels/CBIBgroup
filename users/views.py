from django.shortcuts import render
from users.forms import CustomUserChangeForm
from users.models import CustomUser
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def user_detail(request):
    user = request.user
    return render(request, 'user_detail.html', {'user': user})

def user_edit(request):
    user = request.user
    if request.method == "POST":
        print(request.POST)
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()
            return redirect('user_detail')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'user_form.html', {'form': form})