import re

def validate_email(email: str) -> list:
    """
    사용자가 입력한 이메일 형식을 검증합니다.
    유효하지 않은 경우 ["INVALID_EMAIL"]을 반환하고, 유효하면 빈 리스트를 반환합니다.
    """
    # 빈 문자열 및 None 체크 (Fail-Fast)
    if not email:
        return ["INVALID_EMAIL"]

    # 이메일 검증 정규표현식 패턴
    # [계정명] @ [도메인] . [최상위 도메인] 구조를 강제합니다.
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    # 정규표현식 매칭 확인
    if not pattern.match(email):
        return ["INVALID_EMAIL"]
        
    return []