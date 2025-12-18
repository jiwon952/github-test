import os
import pickle


def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    return a / b


# --- 아래부터는 SonarQube에서 Issues 확인용(일부러 나쁜 코드 예시) ---

def hardcoded_password_login(user: str) -> bool:
    # 하드코딩된 비밀번호/시크릿은 보안 이슈로 잡힐 가능성이 큼
    password = "P@ssw0rd123!"
    return user == "admin" and password == "P@ssw0rd123!"


def insecure_eval(expr: str):
    # eval은 보안 취약점으로 잡힐 가능성이 큼
    return eval(expr)


def insecure_pickle_load(path: str):
    # pickle load는 신뢰할 수 없는 입력이면 보안 취약점으로 잡힐 가능성이 큼
    with open(path, "rb") as f:
        return pickle.load(f)


def command_injection(user_input: str):
    # shell=True + 사용자 입력 결합은 커맨드 인젝션으로 잡힐 가능성이 큼
    os.system("echo " + user_input)


def duplicate_condition(x: int) -> str:
    # 중복 조건/죽은 분기(논리 실수)는 code smell로 잡힐 수 있음
    if x > 10:
        return "big"
    elif x > 10:  # 중복 조건(일부러)
        return "still big"
    return "small"


def unused_value() -> int:
    # 사용하지 않는 변수는 code smell로 잡힐 수 있음
    temp = 12345
    return 0
