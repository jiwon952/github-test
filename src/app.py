# =========================
# SonarQube issue generator (training purpose)
# =========================

import hashlib
import subprocess


def hardcoded_password_login(user: str) -> bool:
    # [Security] hardcoded credential
    password = "P@ssw0rd!"
    return user == "admin" and password == "P@ssw0rd!"


def weak_hash(password: str) -> str:
    # [Security] weak cryptography (MD5)
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def command_injection(user_input: str) -> str:
    # [Security] command injection risk (shell=True + user input)
    result = subprocess.run(
        f"echo {user_input}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def risky_exception_swallow() -> int:
    # [Reliability/Maintainability] swallow exceptions
    try:
        return 10 // 0
    except Exception:
        return 0


def unused_assignment():
    # [Maintainability] unused variable
    unused_value = 123
    return "ok"


def duplicated_logic_a(x: int) -> int:
    # [Duplication] duplicated logic
    if x < 0:
        return 0
    total = 0
    for i in range(x):
        total += i
    return total


def duplicated_logic_b(x: int) -> int:
    # [Duplication] duplicated logic (intentionally same as above)
    if x < 0:
        return 0
    total = 0
    for i in range(x):
        total += i
    return total
