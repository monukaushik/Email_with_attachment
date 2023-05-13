# 1. add openai api key in settings.py 
#          OPENAI_API_KEY =  "api_key"

# 2. then go to views.py file and import 
    
         #   import openai
         #   from django.conf import settings 

# 3. write a function for get the text and fetch the data from open ai

         # def generate_text(request):
         #    if request.method =='POST':
         #       input_text = request.POST.get('searchtext')
         #       openai.api_key = settings.OPENAI_API_KEY
         #       response = openai.Completion.create(
      #             engine="text-davinci-003"    # engine and model for generate details accourding to user
      #             prompt=input_text,
      #             max_tokens=2000,             # no of text which is show on html page 
      #             temperature=1,
      #             stop=None,
         # )
         #    generated_text = response.choices[0].text  // fetch text detail of response data
         #    return render(request,"emailsend.html",{'data':generated_text})

# 4. then go to urls.py and import function from views

#         from emailattachment_app.views import generate_text
#    set a urls ->
#         path('generate_text/', generate_text, name='generate_text'),
