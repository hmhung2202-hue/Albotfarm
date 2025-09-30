from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app running for Zalo OA integration!"

# Webhook endpoint (Zalo sẽ gọi vào đây)
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Webhook verification OK"
    if request.method == "POST":
        data = request.json
        print("📩 Nhận dữ liệu từ Zalo:", data)
        return jsonify({"status": "ok"}), 200

# Zalo domain verify file
@app.route('/zalo_verify.html')
def zalo_verify():
    return send_from_directory(os.getcwd(), 'zalo_verify.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
