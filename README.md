# 2026-1 웹서비스 프로그래밍 미니 프로젝트 (Part 1)

경북대학교 전자공학부 김준석 (2021111675)

## 1. 프로젝트 개요
Flask 프레임워크를 활용하여 간단한 개인 포트폴리오 정보를 제공하는 API 서버를 구축하였습니다. 
Git의 feature 브랜치 전략을 학습하고 적용하는 것을 주 목적으로 합니다.

## 2. 주요 기능 (API 엔드포인트)
- **Home (`/`)**: 본인의 인적사항 및 기술 스택 정보 반환
- **Projects (`/projects`)**: 현재 진행 중인 프로젝트(Flask 포트폴리오) 정보 반환
- **Contact (`/contact`)**: 이메일, GitHub, LinkedIn 등 연락처 정보 반환

## 3. 사용 기술
- **Language**: Python 3.10+
- **Framework**: Flask 3.0.x
- **Version Control**: Git (Branch: main, feature/portfolio-update)

## 4. 실행 방법
```bash
# 관련 패키지 설치
pip install -r requirements.txt

# 서버 실행
python app.py