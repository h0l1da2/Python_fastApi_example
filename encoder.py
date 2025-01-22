import datetime
import pytest
from fastapi.encoders import jsonable_encoder
import json

# 테스트용 데이터 생성
@pytest.fixture
# 여기서 만든 data() 를 테스트 매개변수 (data) 에서 사용함.
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    # with 구문을 사용하여 예외가 발생하는지 확인
    with pytest.raises(Exception):
        # datetime 객체를 JSON으로 변환 시도 (직렬화가 안되므로 예외 발생 예상)
        # `_` <- 해당 값을 사용하지 않겠다는 의미, 해당 값을 변수에 할당하지만 사용하지 않을 때.(이 값은 중요하지 않다.)
        _ = json.dumps(data)

def test_encoder(data):
    # jsonable_encoder 함수를 사용하여 datetime 객체를 JSON으로 변환 가능한 형태로 변환
    out = jsonable_encoder(data)
    # 변환된 데이터가 존재하는지 확인 (None이 아닌지 체크)
    assert out
    # 변환된 데이터(out)를 JSON 문자열로 직렬화하여 정상 작동하는지 확인
    json_out = json.dumps(out)
    # JSON 직렬화 결과가 존재하는지 검증 (예외 발생 없이 올바른 값이 있는지 체크)
    assert json_out
