from datetime import datetime
from model.tag import Tag

def create(tag: Tag) -> Tag:
    """태그 생성"""
    return tag

def get(tag_str: str) -> Tag:
    return Tag(tag=tag_str, created=datetime.now(), secret="hidden")