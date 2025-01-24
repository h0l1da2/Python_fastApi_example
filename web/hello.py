from fastapi import APIRouter, Body, Header, Response

# 전체 웹 애플리케이션을 나타내는 최상위 FastAPI
router = APIRouter()

# URL 경로, 여기서는 GET
@router.get("/hello/hi")
# 경로 함수~
def greet(who):
    return f"Hello {who}!"

@router.post("/hello/hello")
def hello(who: str = Body(embed=True)):
    return f"hello {who}!"

@router.get("/hello/hi-hello")
# fastApi 는 Header() 키를 소문자로 변환하고, 하이픈을 밑줄로 변환한다.
# header 에 있는 who 라는 key 의 값을 가져온다고 생각하면 됨
# who: {who}
def hi_hello(who: str = Header()):
    return f"Hello {who}"

@router.get("/hello/agent")
def get_agent(user_agent: str = Header()):
    return user_agent

@router.get("/hello/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal Body"