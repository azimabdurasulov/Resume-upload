from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View

class HomeView(View):
    def get(self, request):
        candidates = Resume.objects.all()
        form = ResumeForm()
        return render(request, 'myapp/home.html', {"candidates": candidates, "form": form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/home.html', {"form": form})
        
class CondidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(id=pk)
        return render(request, 'myapp/candidate.html', {'candidate': candidate})