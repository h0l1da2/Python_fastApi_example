import fastapi
from collections import namedtuple
from dataclasses import dataclass

def doh2():
    # 이렇게 리스트로 순회할 수도 있지만
    # return ["Hommer: Doh!", "Lisa: A deer", "Marge: A female deer!"]
    # yield 를 사용하면 리스트를 순회하지 않고 객체를 순회해서 다음 yield 를 프린트한다.
    # List와 yeild 의 차이
    # 리스트는 메모리에 리스트를 적재시켜서 값을 꺼내와서 사용해야 함
    # yield 는 하나씩 메모리에 올려서 필요할 때만 데이터 생성 -> 메모리를 거의 사용하지 않으면서 대규모 데이터 순회 가능
    yield "Hommer: Doh!"
    yield "Lisa: A deer"
    yield "Marge: A female deer!"

for line in doh2():
    print(line)

# NamedTuple 을 사용하면 정수 오프셋 또는 이름으로 접근 가능하다.^_^
CreatureNamedTuple = namedtuple("CreatureNameTuple", "name, country, area, description, aka")
namedtuple_thing = CreatureNamedTuple("yeti", "CN", "Himalata", "Hirsute HImalayan", "Abominde Snowman")

print("Name is", namedtuple_thing[0])
print("Name is", namedtuple_thing.country)

@dataclass
class CreatureDataClass():
    name: str
    country: str
    area: str
    description: str
    aka: str

dataclass_thing = CreatureDataClass(
    "yeti",
    "CN",
    "Himalatas",
    "Hirsute Himalayan",
    "Abominabnle Snowman"
)
print("NAME IS", dataclass_thing.name)
