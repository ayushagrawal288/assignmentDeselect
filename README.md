# Image Management Api

## Steps to Buid  
You need to have Python3 and Pip 3 for this to run  
```
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
``` 
## APIs  
```
baseurl=http:127:0.0.1:8000(if you are running locally)  
```
Register a User  
Request:  method=(post)  
```
baseurl/api/register   
parameters =   
{  
	'username': username  
  'password': password  
}  
Response = {  
  'status': 'success'/'fail',  
  'err': 'error message'(if error exits)  
} 
```
  
## Get acess token  
Request  
```
baseurl/api/get_auth_token method=(post)  
parameters =   
{  
  'username': username  
  'password': password  
}  
Response = {  
  'token': acces_token  
}  
``` 
## Upload  
baseurl/api/upload   
Method = (get)
```
Header = {  
    'Authorization': 'token '+access_token   
}    
Parameters = {  
  'file': filename (if filename if None or 'all' then it will provide list of all the images of the user else single image)  
}  

Response:  
if file==None or 'all'  
{  
 'status': 'success',  
 'files': list of all the files  
}  
else  
required file is displayed  
  
Method = (post)  
Request = {  
  'file' : upload image  
}  
Response = {  
 'status': 'success',   
}   
```  
Method = (patch)  
```
Request = {  
  'file' : upload new image,  
  'filename': current image to be replaced  
}  
Response = {  
 'status': 'success',   
}  
``` 
Method = (delete)  
```
Request = {  
  'filename': 'image to be deleted'  
}  
Response = {  
 'status': 'success',   
}  
```
