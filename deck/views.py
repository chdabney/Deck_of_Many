from django.shortcuts import render

# Create your views here.
def index_view(request):

    template_name = "index.html"
    greet = "hi"
    context = {"greetings": greet}
    return render(request, template_name,context)