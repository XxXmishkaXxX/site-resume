from django.shortcuts import render
from django.views import View


# Create your views here.
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class MainPage(View):

    def get(self, request):
        return render(request, 'index.html')
