
class Tiger:
    def jump(self):
        print("호랑이 점프")
    def cry(self):
        print("호랑이 어흥!")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 으르렁~")

# 다중으로 상속 받을 때 이름 충돌
class Liger(Tiger, Lion):
    def play(self):
        print("라이거와 놀기")


# 인스턴스 생성
l = Liger()
l.cry()
print("내부의 상속 순서 튜플:{0}".format(Liger.__mro__))



        
