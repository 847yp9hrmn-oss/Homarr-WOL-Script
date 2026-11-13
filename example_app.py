from flask import Flask, jsonify
from wakeonlan import send_magic_packet

app = Flask(__name__)

# Machine mac address
MACHINE_MAC = "00:00:00:00:00:00"  # Replace with the actual MAC address of the machine you want to wake

# This binds both the root URL '/' (which Homarr pings) and '/wake' to this function
@app.route('/', methods=['GET', 'POST'])
@app.route('/wake', methods=['GET', 'POST'])
def wake_machine():
    try:
        # Broadcast packet straight to mac address.
        wake(MACHINE_MAC)
        return jsonify({"status": "success", "message": f"WoL packet sent to Machine ({MACHINE_MAC})"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
