from datetime import datetime
# Java 에서 Object 를 임의로 정의하는 것과 다르게
# BaseModel 을 쓰면 Validation, Serealizable(직렬화), 타입 변환 등을 해줌 @Valid @NotNull 등등 자동 느낌?
from pydantic import BaseModel

class TagIn(BaseModel):
    tag: str

class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str

class TagOut(BaseModel):
    tag: str
    created: datetime

data = Tag(tag="ai", created=datetime.now(), secret="hidden")
print(data.json())
print(data.dict())