from flask import Blueprint, jsonify

# Create Blueprint
student_bp = Blueprint('student', __name__)

# Sample route
@student_bp.route('/students', methods=['GET'])
def get_students():
    return jsonify({
        "message": "Student API is working",
        "students": []
    })