from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contactSimpleView(request):
    userName = ''
    if('name' in request.session):
        userName = request.session['name']
    myContactForm = ContactForm()

    if(request.method == 'POST'):
        # salvare
        myContactForm = ContactForm(request.POST)
        if(myContactForm.is_valid()):
            myContactForm.save()
            messages.success(request, 'Contact form saved')
            return redirect(reverse_lazy('contact'))

    return render(request, 'contact/simple.html', { 
        'form': myContactForm,
        'name': userName
    })

class ContactViewV1(TemplateView):
    template_name = 'contact/v1.html'

    def get(self, request):
        myContactForm = ContactForm()
        return render(request, self.template_name, { 'form':myContactForm } )

    def post(self, request):
        myContactForm = ContactForm(request.POST, request.FILES)
        if(myContactForm.is_valid()):
            myContactForm.save()
            messages.success(request, 'Contact form saved V1')
            return redirect(reverse_lazy('contact_v1'))
        return render(request, self.template_name, { 'form':myContactForm } )


class ContactFormV2View(FormView):
    template_name = 'contact/v2.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_v2')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Contact form saved V2')
        return super().form_valid(form)

