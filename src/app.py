import subprocess
import sys

def bad_compare(x):
    # BUG: 항상 True/False 흐름이 이상해질 수 있음 (코드 스멜)
    return x is 1000

def division(a, b):
    # BUG: 0으로 나누면 런타임 에러 가능
    return a / b

def index_out_of_range(arr):
    # BUG: 인덱스 에러 가능
    return arr[len(arr)]

def null_deref():
    # BUG: NoneType 사용 (AttributeError)
    obj = None
    return obj.upper()

def duplicate_logic(n):
    # CODE SMELL: 중복 로직(duplicated blocks) 유도
    if n > 0:
        result = n * 2 + 10
        result = result - 3
        result = result * 5
        return result
    else:
        result = n * 2 + 10
        result = result - 3
        result = result * 5
        return result

def unreachable():
    # CODE SMELL: 도달 불가능 코드
    return 1
    print("never")

def useless():
    # CODE SMELL: 사용하지 않는 변수
    temp = 123
    return 0

def command_shell(user_input):
    # CODE SMELL/BUG(환경에 따라): shell=True는 위험/경고 대상이 될 수 있음
    subprocess.run("echo " + user_input, shell=True, check=False)

if __name__ == "__main__":
    # 일부는 실행되면 에러가 나지만, 실행이 목적이 아니라 "정적 분석 이슈" 확인용
    print(division(1, 0))
import hashlib
import subprocess

def hotspot_hardcoded_password():
    password = "P@ssw0rd"   # ← 이 패턴은 Hotspot으로 잡히는 경우가 많음
    return password

def hotspot_weak_crypto(pw: str) -> str:
    return hashlib.md5(pw.encode("utf-8")).hexdigest()  # 약한 해시

def hotspot_command_injection(user_input: str):
    subprocess.run("echo " + user_input, shell=True, check=False)  # shell=True
