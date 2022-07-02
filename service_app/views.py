"""
Contains business logic.
Try/Except is written only in the Home view.
Any Exception raised will be caught in the Home view -
as the main Processing method is called from Home.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
import urllib.request
import pyttsx3
from service_app import models
from service_app import tasks
from gtts import gTTS

from django.urls import reverse



@require_http_methods(['GET', 'POST'])
def into_audio(request):
    
    if request.method == 'POST':
        text = request.POST.get('text')
        myobj = gTTS(text=text, lang='ru')   
        myobj.save("static/speech.wav")
        music = 'ok'
        samples = models.AudioDataModel.objects.all()
        pending_jobs = models.AudioDataModel.objects.filter(status='PEN').count()
        show_timer = False
        context = {
            'music': music,
        }
        return render(request, 'service/home.html', {'samples': samples, 'show_timer': show_timer, 'music': music}) 
    else:
        pass
    
    return HttpResponseRedirect('/')
    

@require_http_methods(['GET', 'POST'])
def home_view(request):
    """
    Main Home page
    """
    try:
        if request.method == 'GET':
            samples = models.AudioDataModel.objects.all()
            pending_jobs = models.AudioDataModel.objects.filter(status='PEN').count()
            show_timer = False
            return render(request, 'service/home.html', {'samples': samples, 'show_timer': show_timer})

        uploaded_file = request.FILES['uploaded_file']
        audio_data = models.AudioDataModel.objects.create(uploaded_file=uploaded_file)

        tasks.process_uploaded_file(audio_data.id)

        return HttpResponseRedirect('/')

    except Exception as e:

        audio_data.status = 'ERR'
        audio_data.error_occurred = True
        audio_data.error_message = str(e)
        audio_data.save()

        return HttpResponse(f'Error: {str(e)}')
        
        

 