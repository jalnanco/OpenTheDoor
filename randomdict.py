# -*- coding: utf-8 -*-
from collections import UserDict
import random


# RandomDict 는 르망 프로젝트에서 만들었던 RandomChoicableDict2 와
# 동일하다. 세 프로젝트 모두에서 이 코드가 쓰이길래 kanu 에 디파인을
# 해둔다. 이름이 바뀐게 맘에 안들면 import 할때 as 로 이름바꿔쓰거나
# alias 잡아서 써라. RandomChoicableDict2 라는 이름이 급조된 이름이라
# 이번에 이름을 바꾼것. 이번이름도 구리지만.
#
# 프로젝트마다 추가기능이 필요할텐데 잘 생각해보고 다른이들도 쓸것
# 같으면 바로 추가하고 자신의 프로젝트에서만 쓸것 같다 싶으면 개별로
# 상속받아 확장해서 쓸것.
class RandomDict(UserDict):
    """랜덤하게 값을 뽑아올수 있는 딕셔너리

    random.choice 나 random.sample 이 시퀀스 타입만 받기 때문에
    딕셔너리를 바로 넘길수가 없었다. 그렇다고 .keys() 를 매번 해줄수도
    없는 일이고.. ( .keys 가 내부적으로 캐싱을 해주는지 정확히
    찾아보지는 않았으나 id(d.keys()) 값이 달라지는걸 봐선 캐싱은
    안해주는것 같다 )

    그래서 key -> value 외에도 key 를 리스트 형태로 따로 들고있도록
    하는 딕셔너리 처럼 돌아가는 컨테이너를 작성해야 했고, 이게 그녀석.

    삭제때문에 좀 트릭이 쓰였는데 특정 키를 삭제할때 리스트에서 해당
    키를 순차검색해서 지울수는 없으므로 딕셔너리의 값으로 리스트의
    인덱스도 같이 들고 있도록 했다. __delitem__ 코드를 읽어보면 이해가 갈것.
    """
    def __init__(self, data=None):
        super().__init__()
        self.__d = {}  # Key -> [Value, Index]
        self.__l = []  # [Key]
        if data:
            for k, v in data.items():  # Python 3에서는 .items() 사용
                self[k] = v

    def __len__(self):
        return len(self.__l)

    def __getitem__(self, key):
        return self.__d[key][0]  # Value 만 리턴해준다.

    def __setitem__(self, key, value):
        """__setitem__ 처리도중 컨텍스트 스위칭이 일어난다면 망한다. 현재
           우리코드들이 gevent 기반이라 lock 을 걸지 않았지만 thread
           기반의 코드를 작성한다면 lock 이 필수
        """
        if key in self.__d:
            # 갱신이라면, 즉 기존에 키가 있었다면
            # 값만 바꾸면 된다.
            self.__d[key][0] = value
        else:
            # 새로 추가하는 거라면, 즉 기존에 키가 없었다면
            # __l 에 이 키를 추가하고 이 인덱스를 이용하여
            # [값, 인덱스] 의 리스트를 키의 값으로 추가한다.
            self.__l.append(key)
            self.__d[key] = [value, len(self.__l) - 1]

    def __delitem__(self, key):
        _, index = self.__d.pop(key)          # 딕셔너리에서 해당 키 제거하며 인덱스 확보
        if index == len(self.__d):
            self.__l.pop()                    # 이미 리스트의 마지막이라면 걍 삭제
        else:
            self.__d[self.__l[-1]][1] = index  # 리스트의 마지막 키를 읽어서 그 키의 인덱스가 지워질 인덱스를 가리키도록 변경
            self.__l[index] = self.__l[-1]     # 리스트의 마지막 키를 지워질 인덱스로 복사
            self.__l.pop()                     # 리스트의 마지막 키를 삭제

    def __iter__(self):
        return self.__d.iterkeys()

    def choice(self):
        return random.choice(self.__l)

    def sample(self, number):
        try:
            return random.sample(self.__l, number)
        except ValueError:
            # number 가 __l 보다 큰경우 여기 떨어지는데 그냥 __l 리턴해줬다.
            # 즉 3 개 가진 상태에서 10개 랜덤으로 달라고 하면 걍 3개 리턴해주는 식.
            return self.__l

    def clear(self):
        self.__d.clear()
        self.__l = []


if __name__ == "__main__":
    import doctest
    doctest.testmod()
