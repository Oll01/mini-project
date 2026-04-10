"""Data management module for the portfolio.

This module acts as the single source of truth for the project data,
defining the data models and storing the mock database.
"""

from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Project:
    """Represents a portfolio project.

    This dataclass serves as the primary data model for an individual project,
    storing essential details like the title, description, and technology stack.

    Attributes:
        id (int): The unique identifier for the project.
        title (str): The name of the project.
        description (str): A detailed summary of the project's purpose and features.
        tech_stack (List[str]): A list of technologies and tools used (e.g., Python, Flask).
        github_url (str): The URL linking to the project's GitHub repository.
    """
    id: int
    title: str
    description: str
    tech_stack: List[str]
    github_url: str

# A mock database containing the list of portfolio projects.
PROJECTS = [
    Project(
        id=1,
        title="Flask 기반 개인 포트폴리오 웹 서비스",
        description="경북대학교 전자공학부 미니 프로젝트의 일환으로 제작된, Flask API 기반의 개인 포트폴리오 서비스입니다. Git 브랜치 전략을 활용하여 개발되었습니다.",
        tech_stack=["Python", "Flask", "Git"],
        github_url="https://github.com/Oll01/mini-project"
    )
]