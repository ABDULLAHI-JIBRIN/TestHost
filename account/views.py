from django.shortcuts import render,redirect
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} your account created successfull, you can now log')
            return redirect('login')


    else:
        form = RegisterForm()

    
    return render(request, 'account/register.html', {'form':form})


def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'profile updated successfully!')
            return redirect('account:profile')

    else:

        u_form = UserUpdateForm(instance = request.user, )
        p_form = ProfileUpdateForm( instance = request.user.profile )



    return render(request, 'account/update.html',{
        'u_form':u_form,
        'p_form':p_form
    })




def profile(request):
    return render(request,'account/profile.html')
