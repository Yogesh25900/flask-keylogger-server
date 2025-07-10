# Real-Time Keylogger Simulation (Educational Use Only)

This is a real-time **keylogger simulation system** built with Python for **ethical learning and demonstration purposes only**. It captures keystrokes on your local machine and sends them to a Flask-SocketIO server, where they are displayed live in the browser.

>  **Disclaimer**  
> This project is strictly intended for educational use in a **controlled environment** on your own system. **Do not use this tool on others’ devices or networks**. Misuse may be illegal and unethical.

---

##  Features

- 🔹 Captures every keystroke using `pynput`
- 🔹 Sends keystrokes to a Flask backend in real-time
- 🔹 Displays live keystroke logs in a web browser using WebSocket (`flask-socketio`)
- 🔹 Deployed on [Railway](https://railway.app/) with zero downtime
- 🔹 Smooth UI updates with character limiting for performance
- 🔹 Optimized with a queue and background thread to prevent lag and freezing

---

##  Tech Stack

| Component      | Description                         |
|----------------|-------------------------------------|
| Python         | Core language                       |
| pynput         | Key capture                         |
| Flask          | Web framework                       |
| Flask-SocketIO | Real-time communication (WebSocket) |
| Railway        | Cloud deployment platform           |
| HTML/CSS/JS    | Live log viewer frontend            |

---



##  How It Works

1. `keylogger.py` runs on your machine and captures keys.
2. Each key is added to a queue to prevent lag.
3. A background thread sends characters to the server (`/upload`) via HTTP POST.
4. Flask-SocketIO server broadcasts each keystroke to connected browsers in real time.
5. Browser displays the log with auto-scroll and character limit to keep things smooth.

---

##  Deployment

You can deploy this on [Railway](https://railway.app/) using:

- `requirements.txt`
- `Procfile`
- `server.py`

