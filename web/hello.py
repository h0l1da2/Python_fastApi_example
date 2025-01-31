from fastapi import APIRouter, Body, Header, Response
import asyncio
# 전체 웹 애플리케이션을 나타내는 최상위 FastAPI
router = APIRouter()

@router.get("/hi")
async def greet():
    # 비동기 함수에서는 호출 전에 await 을 추가해야 함. 이 함수는 이거 기다리는동안 CPU로 다른 작업을 할 수 있단 얘기
    # 위에 async 를 붙였기 때문에 그 함수에는 비동기 함수를 호출할 수 있음.
    await asyncio.sleep(1)
    return "Hello World"

# # URL 경로, 여기서는 GET
# @router.get("/hello/hi")
# # 경로 함수~
# def greet(who):
#     return f"Hello {who}!"

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