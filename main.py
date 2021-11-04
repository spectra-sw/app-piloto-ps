from flask import Flask
from flask import Flask, render_template, url_for, request, redirect, make_response, Response, session, send_file, jsonify, send_from_directory
import cv2
import numpy as np
import base64
from test import api
import json 
import requests
app = Flask(__name__)



@app.route('/',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    
@app.route('/menu',methods=['GET'])
def menu():
    res=api('142900.60b8f3a26b8f1.jpg')
    res = json.loads(res)
    print(res["detected"])
    return render_template("menu.html",res=res)

@app.route('/analizar',methods=["POST"])
def analizar():
    if request.method == 'POST':
        
        data=json.loads(request.data.decode())
        #print(data['file'])
        
        fphoto  = data['file']
        img = readb64(fphoto)
        filef = "static/images/" + "test.jpg"
        cv2.imwrite(filef,img)
        
        res=api("static/images/test.jpg")
        res = json.loads(res)
        return render_template('resultado.html',res=res["detected"])
        
        
        
    return "ok"

def readb64(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

if __name__ == "__main__":
    
    app.run(debug=True)