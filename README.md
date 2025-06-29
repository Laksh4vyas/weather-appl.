# 🌦️ Weather Application — Python + Tkinter

A simple yet elegant **Weather App** built using **Python** and **Tkinter**. This application allows users to fetch **real-time weather information** (temperature, humidity, and condition) for any city using the **OpenWeatherMap API** — all within a clean and user-friendly GUI.

| Main GUI |
|----------|
| ![Weather GUI](./assets/weather-app.png) |

---

## 🔑 Key Features

- 🖼️ **Graphical Interface** using Tkinter  
- 🌐 **Real-Time Weather** data via OpenWeatherMap API  
- 💧 Displays **Temperature**, **Weather Conditions**, and **Humidity**  
- 🧠 **Error Handling** for invalid inputs or network issues  
- 🖼️ Weather icon/image integration using **Pillow (PIL)**

---

## 🗂️ Project Structure

weather-app/
├── GUI - Weather Application.py # Main application file
├── assets/
│ └── weather-icon.png # Weather image (optional)
├── requirements.txt # Dependencies list
└── README.md # Project documentation



---

## ⚙️ Technologies Used

| Module   | Description                          |
|----------|--------------------------------------|
| `tkinter` | GUI interface (built-in with Python) |
| `requests` | Fetching data from OpenWeatherMap API |
| `Pillow (PIL)` | To display weather icons (optional) |

---

## 🔧 Installation Guide

### ✅ Prerequisites

Ensure Python is installed on your system.

```bash
python --version
🚀 Steps to Run Locally
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/weather-app.git
cd weather-app
Install Required Modules

Via requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install Pillow
pip install requests
Insert Your OpenWeatherMap API Key

Sign up at https://openweathermap.org/api

Copy your API key

Replace the value of api_key = "your_api_key_here" in your Python code

Run the App

bash
Copy
Edit
python "GUI - Weather Application.py"
📌 How to Use
🏙️ Enter the name of a city

☁️ Click the Get Weather button

🌡️ View the live temperature, condition, and humidity

💡 Future Enhancements
📍 Auto-detect user location using IP

🌐 Multi-language support

🌈 Theme switcher (dark/light mode)

📉 5-day forecast graph

🙏 Acknowledgements
OpenWeatherMap API

Pillow (PIL)

Tkinter

📄 License
This project is licensed under the MIT License — you're free to use, modify, and distribute.

👨‍💻 Author
Laksh Vyas
📧 lakshvyas462006@gmail.com
🔗 LinkedIn (optional)
🌐 Portfolio: Coming Soon

⭐ Support
If you found this project helpful:

🌟 Star the repo

🛠️ Fork and enhance it

📣 Share with others

Happy Coding! 🔥
