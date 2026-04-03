from flask import Flask, jsonify, request, render_template
from dataclasses import asdict
from validation import validate_email
from data import PROJECTS
from config import OWNER

app = Flask(__name__)

# 악취 4번 해결: 중복 응답 구조 제거를 위한 Helper 함수
def make_response(page, data):
    response = {"page": page}
    response.update(data)
    return jsonify(response)

@app.route("/")
@app.route("/home")
def home():
    return make_response("home", OWNER)

@app.route("/projects")
def projects():
    return make_response("projects", {
        "total": len(PROJECTS),
        "projects": [asdict(p) for p in PROJECTS]
    })

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p.id == project_id), None)
    if project is None:
        return jsonify({"error": "Project not found"}), 404
    return make_response("project_detail", {"project": asdict(project)})

@app.route("/contact")
def contact():
    return make_response("contact", {
        "name": OWNER["name"],
        "email": OWNER["email"],
        "github": OWNER["github"],
        "linkedin": OWNER["linkedin"],
        "message": OWNER["message"]
    })

@app.route('/api/contact', methods=['POST'])
def contact_route():
    data = request.get_json() or {}
    email = data.get('email', '')
    errors = validate_email(email)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400
    return jsonify({"success": True, "message": "이메일이 성공적으로 접수되었습니다!"}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Page not found"}), 404

@app.route("/inquiry")
def inquiry_page():
    return render_template("inquiry.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)