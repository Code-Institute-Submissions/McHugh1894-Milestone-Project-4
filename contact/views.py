from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ Customer contact form view """
    contact_form = ContactForm
    if request.method == "POST":
        form_data = {
            'name': request.POST.get('name', ''),
            'email': request.POST.get('email', ''),
            'message': request.POST.get('message', '')
        }
        print(f"FORM_DATA: {form_data}")
        form = contact_form(form_data)

        if form.is_valid():
            print("Form is valid")
            send_mail(
                form_data['name'] + " - " + form_data['email'],
                form_data['message'],
                'fitbeast001@gmail.com',
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
        messages.success(
            request, 'We have received your queries, we will get back to you within 2 business days, Thanks!'  # noqa: E501
            )
        return redirect('contact')
    context = {
        'form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
