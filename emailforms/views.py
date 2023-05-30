from django.shortcuts import render, redirect
from emailforms.forms import *


# Create your views here.
def send(request):
    return None


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            return redirect('contact')
    else:
        form = EmailForm()
    return render(request, 'emailforms/contact-form.html', {'form': form})