import requests
from tkinter import *
from tkinter import messagebox

API_KEY = "YOUR_API_KEY"

# ---------------------
# Weather Function
# ---------------------

def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a city name!"
        )
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)

        data = response.json()

        if data["cod"] != 200:

            messagebox.showerror(
                "Error",
                "City not found!"
            )
            return

        city_label.config(
            text=f"📍 {data['name']}"
        )

        temp_label.config(
            text=f"🌡 Temperature: {data['main']['temp']} °C"
        )

        humidity_label.config(
            text=f"💧 Humidity: {data['main']['humidity']}%"
        )

        wind_label.config(
            text=f"🌬 Wind Speed: {data['wind']['speed']} m/s"
        )

        condition_label.config(
            text=f"☁ Condition: {data['weather'][0]['main']}"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

# ---------------------
# GUI
# ---------------------

root = Tk()

root.title("Weather Dashboard Pro")

root.geometry("600x500")

root.resizable(False, False)

title = Label(
    root,
    text="🌦 Weather Dashboard Pro",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)

city_entry = Entry(
    root,
    width=30,
    font=("Arial", 14)
)

city_entry.pack(pady=10)

Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
).pack()

city_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold")
)

city_label.pack(pady=20)

temp_label = Label(
    root,
    text="",
    font=("Arial", 14)
)

temp_label.pack()

humidity_label = Label(
    root,
    text="",
    font=("Arial", 14)
)

humidity_label.pack()

wind_label = Label(
    root,
    text="",
    font=("Arial", 14)
)

wind_label.pack()

condition_label = Label(
    root,
    text="",
    font=("Arial", 14)
)

condition_label.pack()

root.mainloop()