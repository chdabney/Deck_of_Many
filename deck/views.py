import json
from django.shortcuts import render
from django.views import View
import json



# Create your views here.
class IndexView(View):
    template_name = "index.html"
  
    def get(self, request):
        json_data = open('./cards.json')
        data = json.load(json_data)
        json_data.close
        
        context = {"data": data}
        return render(request, self.template_name, context)