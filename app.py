from flask import Flask, jsonify, request, render_template
from flasgger import Swagger  # Swagger UI 생성을 위해 추가
from dataclasses import asdict
from validation import validate_email
from data import PROJECTS
from config import OWNER

app = Flask(__name__)
swagger = Swagger(app)  # Flasgger 초기화

# 악취 4번 해결: 중복 응답 구조 제거를 위한 Helper 함수
def make_response(page, data):
    """Creates a standardized JSON response format.

    This helper function merges the page name and the provided data
    into a single dictionary to prevent code duplication (DRY principle).

    Args:
        page (str): The name of the current page or endpoint.
        data (dict): The data dictionary to be included in the response.

    Returns:
        flask.Response: A JSON response containing the page name and data.
    """
    response = {"page": page}
    response.update(data)
    return jsonify(response)

@app.route("/")
@app.route("/home")
def home():
    """Retrieves the home page data.

    This endpoint returns the basic profile information of the portfolio owner.

    ---
    tags:
      - Portfolio API
    responses:
      200:
        description: Owner information successfully retrieved.
    """
    return make_response("home", OWNER)

@app.route("/projects")
def projects():
    """Retrieves a list of all projects.

    This endpoint returns the total count and the detailed list of all projects
    managed in the portfolio database.

    ---
    tags:
      - Project API
    responses:
      200:
        description: A list of projects successfully retrieved.
        schema:
          type: object
          properties:
            total:
              type: integer
              description: Total number of projects.
            projects:
              type: array
              description: List of project objects.
    """
    return make_response("projects", {
        "total": len(PROJECTS),
        "projects": [asdict(p) for p in PROJECTS]
    })

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    """Retrieves details of a specific project by its ID.

    This endpoint searches for a project using the provided project ID
    and returns its full details if found.

    ---
    tags:
      - Project API
    parameters:
      - name: project_id
        in: path
        type: integer
        required: true
        description: The unique identifier of the project to retrieve.
    responses:
      200:
        description: Project details successfully retrieved.
      404:
        description: A project with the specified ID was not found.
    """
    project = next((p for p in PROJECTS if p.id == project_id), None)
    if project is None:
        return jsonify({"error": "Project not found"}), 404
    return make_response("project_detail", {"project": asdict(project)})

@app.route("/contact")
def contact():
    """Retrieves the contact information.

    This endpoint returns specific contact details such as email, GitHub,
    and LinkedIn URLs of the portfolio owner.

    ---
    tags:
      - Portfolio API
    responses:
      200:
        description: Contact information successfully retrieved.
    """
    return make_response("contact", {
        "name": OWNER["name"],
        "email": OWNER["email"],
        "github": OWNER["github"],
        "linkedin": OWNER["linkedin"],
        "message": OWNER["message"]
    })

@app.route('/api/contact', methods=['POST'])
def contact_route():
    """Submits a contact inquiry email.

    This endpoint receives an email address via a POST request, validates
    its format, and returns a success or error message accordingly.

    ---
    tags:
      - Inquiry API
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: test@knu.ac.kr
              description: The email address of the sender.
    responses:
      200:
        description: Email successfully validated and accepted.
      400:
        description: Invalid email format submitted.
    """
    data = request.get_json() or {}
    email = data.get('email', '')
    errors = validate_email(email)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400
    return jsonify({"success": True, "message": "이메일이 성공적으로 접수되었습니다!"}), 200

@app.errorhandler(404)
def not_found(error):
    """Handles 404 Not Found errors.

    Args:
        error: The default error object raised by Flask.

    Returns:
        flask.Response: A JSON response with a 404 error message.
    """
    return jsonify({"error": "Page not found"}), 404

@app.route("/inquiry")
def inquiry_page():
    """Renders the inquiry HTML page.

    This endpoint serves the frontend HTML template for user inquiries.
    It is not a JSON API endpoint.

    ---
    tags:
      - UI Pages
    responses:
      200:
        description: HTML page rendered successfully.
    """
    return render_template("inquiry.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)