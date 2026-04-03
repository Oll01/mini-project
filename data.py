from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Project:
    id: int
    title: str
    description: str
    tech_stack: List[str]
    github_url: str

PROJECTS = [
    Project(
        id=1,
        title="Flask 기반 개인 포트폴리오 웹 서비스",
        description="경북대학교 전자공학부 미니 프로젝트의 일환으로 제작된, Flask API 기반의 개인 포트폴리오 서비스입니다. Git 브랜치 전략을 활용하여 개발되었습니다.",
        tech_stack=["Python", "Flask", "Git"],
        github_url="https://github.com/Oll01/mini-project"
    )
]