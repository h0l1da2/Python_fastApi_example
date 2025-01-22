from datetime import datetime
from model.tag import TagIn, Tag, TagOut
import service.tag as service
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, 
                   created=datetime.now(), 
                   secret="shit!")
    service.create(tag)
    return tag_in

# response_model -> 이거 응답 직렬화 할 때 TagOut 사용하라는 뜻
@app.get("/{tag_str}", response_model=TagOut)
# tag_str(string 타입)을 가져오고, TagOut 타입으로 리턴하라는 뜻
# public TagOut getOne(@Request~~ String tag_str) <- Java 이것과 동의어
def get_one(tag_str: str) -> TagOut:
    tag: Tag = service.get(tag_str)
    return tag