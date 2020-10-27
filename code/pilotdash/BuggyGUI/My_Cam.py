import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
import statistics
root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('My Cam')
frame.config(background='light blue')
label = Label(frame, text="My Cam",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)
def madFilter(dataArr, threshold =3):
  """
  (list),(float) -> (float)
  Description: Calculate of the last point is an outlier depending on the threshold among the given set of points and returns the value that  should be replaced if it is an outlier. 
  >>> sampleVal = madFilter([5,4,4,4,4,5,3,3,1,1,2,2,5])
  >>> sampleVal
  5
  """
  bArr = []
  medianVal = statistics.median(dataArr)
  for element in dataArr:
    bArr.append(abs(medianVal - element))
  madValue =  statistics.median(bArr)
  if(bArr[-1] > threshold*madValue):
    return medianVal
  else :
    return dataArr[-1]
import doctest
doctest.testmod()
data = np.genfromtxt("logAngles.txt", delimiter=",", names=["date&time","raw_yaw" ,"filter_yaw","smooth_yaw" , "raw_pitch","filter_pitch","smooth_pitch" ])
BUFFERSIZE = 15
dataBuffer = [0]*BUFFERSIZE
print(type(data))



def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contribute")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="My Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()
def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()
def graph():
    plt.figure(1)
    plt.title("Raw Data")
    plt.plot(data['raw_yaw'])
    plt.xlabel("Time(in Seconds)")
    plt.ylabel("Changes in Angles(in Degree)")
    plt.legend("Raw Data")
    plt.show()
def graph1():
    plt.figure(2)
    plt.title("Mad Filter Output")
    plt.plot(data['filter_pitch'],color='red')
    plt.xlabel("Time(in Seconds)")
    plt.ylabel("Changes in Angles(in Degree)")
    plt.legend("Filtered Data")
    plt.show()
def graph2():
    plt.figure(3)
    plt.title("Spline Curve")
    plt.plot(data['smooth_pitch'],color='orange')
    plt.xlabel("Time(in Seconds)")
    plt.ylabel("Changes in Angles(in Degree)")
    plt.legend("Spline Curve")
    plt.show()
   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=graph,text='Raw Data',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=graph1,text='Filtered Data',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=graph2,text='Spline Curve',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but5=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=blink,text='Detect',font=('helvetica 15 bold'))
but5.place(x=5,y=400)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)


root.mainloop()

