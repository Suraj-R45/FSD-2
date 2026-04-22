from flask import Blueprint, request, jsonify

student_bp = Blueprint("student_bp", __name__)

students = []
student_id = 1


@student_bp.route("/students", methods=["POST"])
def create_student():
    global student_id

    data = request.get_json()

    student = {
        "id": student_id,
        "name": data["name"]
    }

    students.append(student)
    student_id += 1

    return jsonify(student), 201


@student_bp.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


@student_bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    for s in students:
        if s["id"] == id:
            return jsonify(s), 200
    return jsonify({"error": "Not found"}), 404


@student_bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    for s in students:
        if s["id"] == id:
            s["name"] = data["name"]
            return jsonify(s), 200

    return jsonify({"error": "Not found"}), 404


@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "deleted"}), 200