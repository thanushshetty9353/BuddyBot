from flask import Flask, render_template, request, jsonify
import google.generativeai as genai  # Import Google AI API

# Initialize Flask app
app = Flask(__name__)

# Set up Gemini API
genai.configure(api_key="AIzaSyB-nwcS9RX6TIODACdIQi8C0IEs6U8_4f8")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-flash")  # Use the latest available Gemini model

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        # Call Gemini API to get the response
        response = model.generate_content(user_message)
        
        # Ensure response is valid
        if response and response.text:
            bot_reply = response.text
        else:
            bot_reply = "Sorry, I couldn't process that request."

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Sorry, there was an error processing your request."})

if __name__ == "__main__":
    app.run(debug=True)
