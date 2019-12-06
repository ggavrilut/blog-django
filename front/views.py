from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    
    template_name = 'front/home.html'
    def get(self, request):
        self.request.session['name'] = 'Gabi'    
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'front/about.html' 


def homeContent(request, value):
    
    return JsonResponse({
        'status': True,
        'message': 'success ' + str(value) + ' ' + str(request.GET['var'])
    })

    # return HttpResponse('success ' + str(value) + ' ' + str(request.GET['var']))