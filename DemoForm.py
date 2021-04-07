# 화면단(DemoForm.ui) + 로직단(DemoForm.py)
import sys
# Qt패키지 로딩 : 패키지명.모듈명
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 미리 만든 화면을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# 다이알로그를 상속받아서 폼클래스를 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__() # 아직 명시하지 못하므로 다 호출
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")

# 직접 이 모듈을 실행했는지 진입점(Entry Point) 체크
if __name__ == "__main__": # 이름이 맞는지 확인
    # 실행 프로세스를 실행(python.exe)
    app = QApplication(sys.argv)
    # 위에 있는 클래스의 인스턴스를 생성
    demoWindow = DemoForm()
    # 창을 보여줌
    demoWindow.show()
    # 지속적으로 실행 : 실행프로세스 실행. (이벤트 루프)
    app.exec_() 
