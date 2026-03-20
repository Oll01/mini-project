# app.py

from flask import Flask, jsonify, request
from validation import validate_email

app = Flask(__name__)

# ============================================================
# Feature 1: Home - Personal Introduction
# ============================================================
@app.route("/")
@app.route("/home")
def home():
    return jsonify({
        "page": "home",
        "name": "김준석",
        "title": "경북대학교 전자공학부 4학년",
        "bio": "AI, 임베디드 시스템, IoT 분야에 관심이 많은 예비 엔지니어입니다.",
        "skills": ["Python", "Flask", "Git", "Java", "SQL", "Embedded Systems"]
    })

# ============================================================
# Feature 2: Projects - Portfolio Project List
# ============================================================
PROJECTS = [
    {
        "id": 1,
        "title": "Flask 기반 개인 포트폴리오 웹 서비스",
        "description": "경북대학교 전자공학부 미니 프로젝트의 일환으로 제작된, Flask API 기반의 개인 포트폴리오 서비스입니다. Git 브랜치 전략을 활용하여 개발되었습니다.",
        "tech_stack": ["Python", "Flask", "Git"],
        "github_url": "https://github.com/Oll01/mini-project"
    }
]

@app.route("/projects")
def projects():
    return jsonify({
        "page": "projects",
        "total": len(PROJECTS),
        "projects": PROJECTS
    })

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if project is None:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({
        "page": "project_detail",
        "project": project
    })

# ============================================================
# Feature 3: Contact - Contact Information (기존 단순 조회용)
# ============================================================
@app.route("/contact")
def contact():
    return jsonify({
        "page": "contact",
        "name": "김준석",
        "email": "see5932@naver.com",  
        "github": "https://github.com/Oll01",
        "linkedin": "https://linkedin.com/in/준석-김",
        "message": "전자공학 및 AI 분야 협업을 환영합니다! 언제든 연락주세요."
    })

# ============================================================
# Feature 4: TADD - Contact Email Validation (POST) - 새로 추가된 부분!
# ============================================================
@app.route('/api/contact', methods=['POST'])
def contact_route():
    data = request.get_json() or {}
    email = data.get('email', '')
    
    # TADD로 만든 검증 로직 실행
    errors = validate_email(email)
    
    if errors:
        return jsonify({"success": False, "errors": errors}), 400
        
    return jsonify({"success": True, "message": "이메일이 성공적으로 접수되었습니다!"}), 200

# ============================================================
# Error Handlers
# ============================================================
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Page not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)