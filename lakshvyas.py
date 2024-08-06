#IMPORTING MODULES
import requests
import tkinter as tk
from tkinter import messagebox
import webbrowser


#MADE A DEF FUNCTION
def get_weather(city_name, api_key):
    """Get the current weather for a given city."""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
#TRYING CONDITIONS
    if data.get("cod") != "404":
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        temp = main.get("temp")
        pressure = main.get("pressure")
        humidity = main.get("humidity")
        weather_description = weather.get("description")
        icon = weather.get("icon")

        weather_info = f"Temperature: {temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description}"
        return weather_info, icon
    else:
        return f"City {city_name} not found.", None
#AGAIN MAKE A DEF FUNCTION
def show_weather():
    """Show the current weather for the given city."""
    city = city_name_entry.get()
    weather_info, icon = get_weather(city, api_key)
    if icon:
        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        icon_response = requests.get(icon_url)
        icon_data = icon_response.content
        icon_image = tk.PhotoImage(data=icon_data)
        icon_label.config(image=icon_image)
        icon_label.image = icon_image
    messagebox.showinfo(f"Weather in {city}", weather_info)

def clear_entry():
    """Clear the city name entry field."""
    city_name_entry.delete(0, tk.END)

def exit_app():
    """Exit the application."""
    root.destroy()

def show_forecast():
    """Show the 5-day forecast for the given city."""
    city = city_name_entry.get()
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(forecast_url)
    data = response.json()

    forecast_info = ""
    for forecast in data.get("list", []):
        forecast_info += f"Date: {forecast.get('dt_txt')}\nTemperature: {forecast.get('main', {}).get('temp')}°C\nPressure: {forecast.get('main', {}).get('pressure')} hPa\nHumidity: {forecast.get('main', {}).get('humidity')}%\nDescription: {forecast.get('weather', [{}])[0].get('description')}\n\n"

    messagebox.showinfo(f"5-Day Forecast for {city}", forecast_info)

def show_map():
    """Show the map for the given city."""
    city = city_name_entry.get()
    map_url = f"https://www.google.com/maps/place/{city}"
    webbrowser.open(map_url)




# GUI Setup
api_key = "79093f1f345cdf842136953249f6223f"  # Replace with your own API key

root = tk.Tk()
root.title("Weather App")
root.configure(bg="#34495e")  # Background color

# Main frame
main_frame = tk.Frame(root, bg="#34495e")
main_frame.pack(pady=20, padx=20)

# Label for city name entry
city_name_label = tk.Label(main_frame, text="Enter City Name:", font=("Helvetica", 20, "bold"), bg="#34495e", fg="#ecf0f1")
city_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Entry box for city name input
city_name_entry = tk.Entry(main_frame, font=("Helvetica", 18), bg="#ecf0f1", fg="#34495e", bd=5, relief="ridge")
city_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Weather icon label
icon_label = tk.Label(main_frame, bg="#34495e")
icon_label.grid(row=1, column=1, padx=10, pady=10)

# Button to check weather
check_weather_button = tk.Button(main_frame, text="Check Weather", command=show_weather, font=("Helvetica", 20, "bold"), bg="#1abc9c", fg="white", activebackground="#16a085", activeforeground="white")
check_weather_button.grid(row=2, column=0, padx=10, pady=10)

# Button to show forecast
forecast_button = tk.Button(main_frame, text="5-Day Forecast", command=show_forecast, font=("Helvetica", 18), bg="#f39c12", fg="white", activebackground="#f7dc6f", activeforeground="white")
forecast_button.grid(row=2, column=1, padx=10, pady=10)

# Button to show map
map_button = tk.Button(main_frame, text="Show Map", command=show_map, font=("Helvetica", 18), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white")
map_button.grid(row=3, column=0, padx=10, pady=10)

# Button to clear entry
clear_button = tk.Button(main_frame, text="Clear", command=clear_entry, font=("Helvetica", 18), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white")
clear_button.grid(row=3, column=1, padx=10, pady=10)

# Button to exit the application
exit_button = tk.Button(main_frame, text="Exit", command=exit_app, font=("Helvetica", 18), bg="#2c3e50", fg="white", activebackground="#34495e", activeforeground="white")
exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
