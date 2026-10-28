
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Student Attendance Management System</h1>
    <p>Welcome to the attendance portal.</p>
    <p>Student: Ramya</p>
    <p>Attendance: 92%</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
