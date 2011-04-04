# Create your views here.
from django.shortcuts import render_to_response
from django.core.files import File
from forms import UploadFileForm
from django.template import RequestContext
from models import Photos
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def handle_uploaded_file(img):
    new_photo = Photos()
    new_photo.photo.save("test_name",img)

def admin(request):
    
    return render_to_response("admin.html")

def add_photo(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))
    new_photo = Photos()
    return render_to_response("add.html")
    
def del_photo(request):
    if request.method == 'POST':
        try:
            photo = Photos.get(id=request.POST['id'])
        except DoesNotExist:
            return render_to_response("del.html",{'errors':'error'})
        photo.delete()
        return HttpResponse('ok')
    else:
        return HttpResponse('need parameter')
            
