
# Create your views here.

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from auth.serializer import UserSerializer
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated, AllowAny

def check_extension(filename):
    if filename != None and filename.split('.')[-1].strip().lower() in ['png', 'jpg', 'jpeg', 'gif']:
        return True
    return False

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

def logout_user(request):
    return render(request, '/accounts/logout.html', {})

def login_form(request):
    return render(request, '/Users/james/Documents/filecompressions/imageManagementRest/templates/accounts/login.html', {})

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.create(serialized.data)
        return Response({ 'status':'success'})
    else:
        return Response({'error':serialized._errors, 'status': 'fail'})


@api_view(['GET','POST', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated,))
def upload_img(request):
    if hasattr(request, 'FILES') and request.FILES.get('file') != None and not check_extension(str(request.FILES.get('file'))):
        return Response({'success': 'fail', 'msg':'only PNG or JPG or GIF format allowed'})
    if request.method == 'POST':
        file = request.FILES['file']
        path = str(request.user)+'/'+str(file)
        file_obj = default_storage.save(path, ContentFile(file.read()))
        return Response({'status': 'success'})
    elif request.method == 'GET':
        path = request.GET.get('file')
        if path == 'all' or path == None:
            urls = []
            try:
                for i in default_storage.listdir(str(request.user))[1]:
                    urls.append('/media/'+str(request.user) + '/' + i)
            except:
                print("No images yet")
            return Response({'status': 'success',' files': urls})
        
        else:
            return redirect('/media/'+str(request.user) +'/'+ path)
    elif request.method == 'PATCH':
        if not request.FILES.get('file'):
            return Response({'status': 'fail', 'msg': 'please provide new image in file attribute'})
        path = str(request.user)+'/'+str(request.data.get('filename') if request.data.get('filename')!= None else request.FILES.get('file'))
        if default_storage.exists(path):
            default_storage.delete(path)
        default_storage.save(path, ContentFile(request.FILES.get('file').read()))
        return Response({'status': 'success'})
    elif request.method == 'DELETE':
        path = str(request.user) +'/'+ str(request.data.get('file'))
        try:
            default_storage.delete(path)
            return Response({'status': 'success'})
        except Exception:
            return Response({'status': 'fail', 'error': Exception.message})
    else:
        return Response({'status': 'fail', 'msg': 'method not allowed'})
