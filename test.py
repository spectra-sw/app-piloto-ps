
import requests

def api(imagen):
    image_file_descriptor = open(imagen, 'rb')
    # Requests makes it simple to upload Multipart-encoded files 
    files = {'file': image_file_descriptor}
    url = 'http://18.235.190.178:5000/predict/'
    
    resp=requests.post(url, files=files).text
    image_file_descriptor.close()
    return resp