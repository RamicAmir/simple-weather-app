# weather_frontend.py
from tkinter import *
from main import get_weather_info

root = Tk()
root.geometry("400x400")  # default size window
root.resizable(0, 0)  # Fixed window size

root.title("Weather App")

city_value = StringVar()


def show_weather():
    city_name = city_value.get()
    weather = get_weather_info(city_name)
    t_field.delete("1.0", "end")
    t_field.insert(INSERT, weather)


Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)

Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()

Button(root, command=show_weather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

Label(root, text="The Weather is:", font='arial 12 bold').pack(pady=10)

t_field = Text(root, width=46, height=10)
t_field.pack()

root.mainloop()
