import cv2
from deepface import DeepFace
from flask import Flask,render_template
import js2py
estate=False
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    
    return render_template("index.html",estate=estate)




@app.route("/moodbased")
def moodbased():
 list1=[]
 count=0
 vid=cv2.VideoCapture(0)
 while count<20:
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        ret,frame=vid.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
        try:
            result=DeepFace.analyze(frame,actions=['emotion'])
            print(result[0]['dominant_emotion'])
            list1.append(result[0]['dominant_emotion'])
            count+=1
            
        except:
            print("no face")
            list1.append("noface")
            count+=1
 vid.release()
 cv2.destroyAllWindows()

 print(list1)
 c=0
 ele=list[0]
 for i in list1:
     curfreq=list1.count(i)
     if curfreq>c:
          c=curfreq
          ele=i


 #print(ele)
 return render_template("index.html",emo=ele,estate=True)




if __name__ == '__main__':
    app.run(debug=True,port=5001)