from flask import Flask

app = Flask(__name__)

# 1. 메인 페이지 (과제 요구사항 / 및 /home 모두 연결)
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home</h1><p>나만의 포트폴리오 웹서비스 메인 화면입니다.</p>"

# 2. 소개 페이지
@app.route("/about")
def about():
    return "<h1>About Me</h1><p>프로젝트를 위한 자기소개 페이지입니다.</p>"

# 3. 연락처 페이지
@app.route("/contact")
def contact():
    return "<h1>Contact</h1><p>연락처 및 이메일 정보를 남기는 페이지입니다.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)