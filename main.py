from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def on_entry_click(event):
    if entry.get() == 'Enter city and country':
        entry.delete(0, "end")
        entry.config(fg='white')


def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter city and country')
        entry.config(fg='grey')


def getWeather():
    try:
        city = entry.get()
        geolocator = Nominatim(user_agent="my_geocoder")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I: %M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=7f92f65c9bbad0af624cad44be979050"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = float(json_data['main']['temp'] - 273.14)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")


# search box
Search_image = PhotoImage(file="img/search.png")
myimage = Label(image=Search_image)
myimage.place(x=220, y=18)

# textfield = tk.Entry(root, justify="center", width=19, font=("poppins", 24, "bold"), bg="#404040", border=0, fg="white")
# textfield.bind('<FocusIn>', on_entry_click)  # bind click to function
# textfield.bind('<FocusOut>', on_focusout)  # bind focus out to function
# textfield.place(x=50, y=40)
# textfield.focus()

# Create entry with default message
entry = Entry(root, justify="center", width=20, font=("poppins", 16), bg="#404040", border=0, fg="grey")
entry.insert(0, 'Enter city and country')  # default text
entry.bind('<FocusIn>', on_entry_click)  # bind click to function
entry.bind('<FocusOut>', on_focusout)  # bind focus out to function
entry.place(x=250, y=45)
# entry.focus()

Search_icon = PhotoImage(file="img/search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=600, y=32)

# logo
Logo_image = PhotoImage(file="img/logo.png")
logo = Label(image=Logo_image)
logo.place(x=300, y=100)

# Bottom box
Frame_image = PhotoImage(file="img/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 16, "bold"))
name.place(x=80, y=120)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=80, y=150)

# label
label1 = Label(root, text="WIND", font=("Helvetica", 16, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 16, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 16, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)
label4 = Label(root, text="PRESSURE", font=("Helvetica", 16, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=580, y=180)
c = Label(font=("arial", 15, "bold"))
c.place(x=580, y=280)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=130, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=470, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=690, y=430)

root.mainloop()
