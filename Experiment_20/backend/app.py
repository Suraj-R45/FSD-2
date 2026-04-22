from flask import Flask
from routes.student_routes import student_bp

def create_app():
    app = Flask(__name__)

    # register blueprint
    app.register_blueprint(student_bp)

    @app.route("/")
    def home():
        return {"message": "Backend Server is running"}, 200

    return app

# IMPORTANT: expose app for pytest and CI
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)