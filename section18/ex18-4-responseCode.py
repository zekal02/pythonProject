'''


서버 요청 - request
서버 응답 - response

http 응답(response)코드
    200번대 응답 : 성공(success)
    300번대 응답:  리다이렉션(Redirection)
    400번대 응답:  클라이언트 에러(Client Error)
        ex) 404 : 찾을 수 없는 페이지(주소 잘 못 입력)
            403 : 권한문제

    500번대 응답: 서버 에러(sever error)
        ex) 503 : 서버가 요청을 처리할 준비가 되지 않음
                    ( 개발자 코드 에러 발생했을 경우)

'''
import requests

url ='https://naver.com'

response = requests.get(url)
print(f'응답 코드:{response.status_code}')