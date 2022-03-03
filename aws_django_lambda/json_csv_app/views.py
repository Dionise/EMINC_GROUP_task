import json
from django.views.generic import TemplateView
from django.http import JsonResponse,HttpResponse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from json_csv_app.utlis import JSONEncoder , Comunication




class HomeView (TemplateView,Comunication):
    template_name = "index.html"  
    def get_context_data(self,  **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['number'] = Comunication.visualize_database().count_documents({})    
        return context

    @csrf_exempt
    def post(self, *args, **kwargs):
        if self.request.method == "POST":
             key = self.request.POST.get('value')
             print(key)
             try:
                 response = Comunication.visualize_database().find_one({
                   "entry.resource.id":key
                   })  
             except Exception:
                  print("Data invalid")
             else:
                 if response:
                   message = json.loads(JSONEncoder().encode(response))  
                   return JsonResponse(message , content_type='application/json')
                 else:
                   res = JsonResponse({'msg': 'User was not found'})
                   return res
        else:
             return JsonResponse({'Error':'Error'})
             
