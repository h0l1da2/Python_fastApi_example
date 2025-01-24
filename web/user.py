from fastapi import APIRouter

router = APIRouter()

# 이하 두 개의 api 는 둘다 string url 을 포함하고 있음
# 그렇기 때문에 먼저 코드상으로 경로가 정해져있는 /user/me 를 추가한 뒤
@router.get("/user/me")
async def user_me():
    return {"user_me": "holiday"}

# /user/{user_name} 경로를 그 후에 추가해주어야만 제대로 동작함
# 순서를 틀리면 /user/me 를 요청했다 하더라도 /user/{user_name} 경로로 인식할 수 있음.
@router.get("/user/{user_name}")
async def user_name(user_name: str):
    return {"user_name": user_name}