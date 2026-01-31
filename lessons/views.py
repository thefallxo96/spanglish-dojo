from django.http import HttpResponse

def home(request):
    return HttpResponse("Spanglish Dojo is live 🥋🔥")
