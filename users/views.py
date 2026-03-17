from django.shortcuts import render
from sms.service import send_otp
from users.forms import SignUpForm
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()

            email = user.email
            send_otp(email)
            return HttpResponse(f'OTP sent to {email}')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})