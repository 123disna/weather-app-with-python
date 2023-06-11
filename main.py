from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import json
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+500")
root.resizable(False,False)


def getWeather():              #it is used to get weather data
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #WEATHER
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c71a14205c0924d4b9845d8807768961'
        response = requests.get(url)
        json_data = json.loads(response.text)

        if 'weather' in json_data:
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temperature = json_data['main']['temp']
            humidity = json_data['main']['humidity']
            pressure = json_data['main']['pressure']
            wind_speed = json_data['wind']['speed']
            temp=int(temperature)-273

        t.config(text=(temp,"°C"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))

        w.config(text=wind_speed)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")

#search box
search_box=PhotoImage(file="boxn.png")
myimage=Label(image=search_box)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#000000",border=0,fg="white")
textfield.place(x=50,y=32)
textfield.focus()

search_icon=PhotoImage(file="icon6.png")
icon_image=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#ffffff",command=getWeather)
icon_image.place(x=350,y=28)

logo_image=PhotoImage(file="weather.png")
logo=Label(image=logo_image)
logo.place(x=150,y=110)

#bottom box
frame_image=PhotoImage(file="bottom.png")
frame_logo=Label(image=frame_image)
frame_logo.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=80)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=110)


label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#6985F6")
label1.place(x=80,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#6985F6")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#6985F6")
label3.place(x=450,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#6985F6")
label4.place(x=700,y=400)

t=Label(font=("arial",60,"bold"),fg="#ee666d")
t.place(x=370,y=130)
c=Label(font=("arial",15,"bold"))
c.place(x=370,y=230)

w=Label(root,text="",font=("arial",20,'bold'),bg="#6985F6")
w.place(x=80,y=430)
h=Label(root,text="",font=("arial",20,'bold'),bg="#6985F6")
h.place(x=280,y=430)
d=Label(root,text="",font=("arial",20,'bold'),bg="#6985F6")
d.place(x=450,y=430)
p=Label(root,text="",font=("arial",20,'bold'),bg="#6985F6")
p.place(x=730,y=430)

root.mainloop()


