from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    '''This view returns contact page and
       posts the contact form information to the db
    '''
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.subject = request.POST['subject'],
            form.message = request.POST['message'],
            form.email = request.POST['email'],
            form.save()
            user_email = ''.join(form.email)
            messages.success(request,
                             f"Thanks { user_email }, Your message has been sent.\
                             We will be in touch shortly.")
            return redirect("home")
        else:
            messages.error(request,
                           'Error: something has gone wrong \
                            please try again later.')
            return redirect('home')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request,
                  template,
                  context)
