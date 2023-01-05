# 해시 테이블 
# 파이썬에서는 해시 테이블을 딕셔너리 라 부른다.
STATUS_CODE = { 200 : "OK", 301: "Moved Permanently"}

def status_code_meaning(number):
    return STATUS_CODE[number]  