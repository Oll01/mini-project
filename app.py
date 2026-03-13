# app.py

from flask import Flask, jsonify

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
        "title": "전자공학 전공 & 예비 개발자",
        "bio": "Passionate developer interested in open source and web technologies.",
        "skills": ["Python", "Flask", "Git", "HTML/CSS"]
    })


# ============================================================
# Feature 2: Projects - Portfolio Project List
# ============================================================
PROJECTS = [
    {
        "id": 1,
        "title": "Web Service Portfolio",
        "description": "A personal portfolio web service built with Flask.",
        "tech_stack": ["Python", "Flask"],
        "github_url": "https://github.com/username/web-service"
    },
    {
        "id": 2,
        "title": "Todo App",
        "description": "A simple task management application.",
        "tech_stack": ["Python", "Flask", "SQLite"],
        "github_url": "https://github.com/username/todo-app"
    },
    {
        "id": 3,
        "title": "Chat Bot",
        "description": "An AI-powered chatbot for customer support.",
        "tech_stack": ["Python", "NLP"],
        "github_url": "https://github.com/username/chatbot"
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
# Feature 3: Contact - Contact Information
# ============================================================
@app.route("/contact")
def contact():
    return jsonify({
        "page": "contact",
        "email": "your.email@example.com",
        "github": "https://github.com/username",
        "linkedin": "https://linkedin.com/in/username",
        "message": "Feel free to reach out for collaboration!"
    })


# ============================================================
# Error Handlers
# ============================================================
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Page not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)