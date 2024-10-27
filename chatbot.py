import os
from PyKakao import KoGPT

# 서비스 키를 환경 변수에서 가져오기
service_key = os.environ.get('KAKAO_API_KEY')

# KoGPT API 인스턴스 생성
GPT = KoGPT(service_key=service_key)

# 다음 문장 만들기
prompt = "인간처럼 생각하고, 행동하는 '지능'을 통해 인류가 이제까지 풀지 못했던"
max_tokens = 64

try:
    result = GPT.generate(prompt, max_tokens, temperature=0.7, top_p=0.8)
    print(result)
except Exception as e:
    print("오류가 발생했습니다:", e)
