from flask import Flask, render_template
app=Flask(__name__)
import picamera as pic
import time

@app.route("/")
def response():
    pass
                                                                       

@app.route("/record")
def control():
    cam=pic.PiCamera()
    cam.vflip=True
    cam.start_preview()
    time.sleep(2)
    cam.start_recording('Video.h264')
    time.sleep(20)
    cam.stop_preview()

@app.route("/snap")
def control2():
    cam=pic.PiCamera()
    cam.vflip=True
    cam.start_preview()
    time.sleep(5)
    cam.capture('Test.jpg')
    cam.stop_preview()
       
        

app.run(debug=True,port=8000,host="")

  
  
   
