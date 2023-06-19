from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from aip import AipFace
import cv2
import base64
from PIL import ImageFont, ImageDraw, Image
from datetime import datetime
import numpy


class Ui_mainForm(object):
    #类变量
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.setWindowModality(QtCore.Qt.NonModal)
        mainForm.resize(691, 432)
        self.pushButton = QtWidgets.QPushButton(mainForm)
        self.pushButton.setGeometry(QtCore.QRect(140, 320, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(mainForm)
        self.tabWidget.setGeometry(QtCore.QRect(370, 210, 301, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 100, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 171, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(200, 60, 75, 24))
        self.comboBox.setObjectName("comboBox")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(210, 40, 54, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(20, 58, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 90, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 60, 51, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_13 = QtWidgets.QLabel(self.tab_1)
        self.label_13.setGeometry(QtCore.QRect(71, 130, 160, 16))
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 90, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 58, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 60, 51, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(71, 130, 160, 16))
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 90, 141, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 58, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 60, 51, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(71, 130, 160, 16))
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox = QtWidgets.QGroupBox(mainForm)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 281))
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 320, 240))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.groupBox_2 = QtWidgets.QGroupBox(mainForm)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 10, 321, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 301, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(80, 25, 160, 120))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.tabWidget.raise_()

        #初始化摄像头
        self.LoadData()
        self.comboBox.addItems([txt[1][2] for txt in self.namelist.items()])
        self.timer_camera = QtCore.QTimer()
        self.cp=cv2.VideoCapture(0)
        self.face_cascade=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
        self.timer_camera.start(20)

        #标志定义
        self.flag=0     #是否已经截取照片
        self.flag1=0    #是否已经检查到人脸
        #标志定义结束

        #连接信号槽
        self.retranslateUi(mainForm)
        self.tabWidget.setCurrentIndex(3)
        self.pushButton.clicked.connect(self.takePicture)  # type: ignore
        self.pushButton_3.clicked.connect(self.faceRecognition)  # type: ignore
        self.pushButton_2.clicked.connect(self.faceRegistration)  # type: ignore
        self.pushButton_4.clicked.connect(self.faceUpdate)  # type: ignore
        self.pushButton_5.clicked.connect(self.faceDeletion)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainForm)
        self.timer_camera.timeout.connect(self.show_camera)

    def show_camera(self):
        flag, self.image = self.cp.read()
        self.image = cv2.flip(self.image, 1, dst=None)
        #cv2.putText(self.image, str(self.cp.get(cv2.CAP_PROP_FRAME_HEIGHT)) + " " + str(self.cp.get(cv2.CAP_PROP_FRAME_WIDTH)),(0, 24), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
        self.py=-100
        self.px=-100
        self.face_image = self.image
        showimage=self.image.copy()
        if len(faces)==0:
            self.flag1=0
        for (x, y, h, w) in faces:
            if h>=200 and w>=200:
                cv2.rectangle(showimage, (x, y), (x + w, y + h), (0, 255, 0), 2)
                self.px, self.py = x, y
                self.flag1=1
                self.face_image = self.image[y:y + h, x:x + w]
        self.label_10.setPixmap(QtGui.QPixmap.fromImage(dis_img(showimage).scaled(320,240)))

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "考勤机"))
        self.pushButton.setText(_translate("mainForm", "拍照备份"))
        self.tab.setAccessibleName(_translate("mainForm", "人脸识别"))
        self.pushButton_3.setText(_translate("mainForm", "识别"))
        self.label_12.setText(_translate("mainForm", "用户组"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainForm", "人脸识别"))
        self.label.setText(_translate("mainForm", "英文名"))
        self.label_2.setText(_translate("mainForm", "中文名"))
        self.label_3.setText(_translate("mainForm", "分  组"))
        self.pushButton_2.setText(_translate("mainForm", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("mainForm", "人脸注册"))
        self.label_4.setText(_translate("mainForm", "分  组"))
        self.label_5.setText(_translate("mainForm", "英文名"))
        self.label_6.setText(_translate("mainForm", "中文名"))
        self.pushButton_4.setText(_translate("mainForm", "更新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainForm", "人脸更新"))
        self.label_7.setText(_translate("mainForm", "分  组"))
        self.label_8.setText(_translate("mainForm", "中文名"))
        self.pushButton_5.setText(_translate("mainForm", "删除"))
        self.label_9.setText(_translate("mainForm", "英文名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainForm", "人脸删除"))
        self.groupBox.setTitle(_translate("mainForm", "摄像头预览"))
        self.groupBox_2.setTitle(_translate("mainForm", "人脸相关操作"))
        self.groupBox_3.setTitle(_translate("mainForm", "照片"))

    def takePicture(self):
        if self.flag1==1:
            self.show=self.face_image
            self.flag=1
            self.label_11.setPixmap(QtGui.QPixmap.fromImage(dis_img(self.show).scaled(160,120)))

    def faceRecognition(self):
        if self.flag1==0:
            self.textBrowser.setText('当前图片未检测到人脸')
        else:
            self.textBrowser.setText("")
        UserGroup=self.comboBox.currentText()


    def faceRegistration(self):
        EnglishName=self.lineEdit.text()
        ChineseName=self.lineEdit_2.text()
        UserGroup=self.lineEdit_3.text()
        if EnglishName== '' or ChineseName=='' or UserGroup=='':
            self.label_13.setText("信息为空！")
            return
        if EnglishName in self.namelist:
            self.label_13.setText('已有此人')
            return
        if self.flag==0:
            self.label_13.setText('未拍照备份')
            return
        # gray = cv2.cvtColor(self.show, cv2.COLOR_BGR2GRAY)
        # faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)
        # if len(faces)==0:
        #     self.label_13.setText("图片无人脸")
        #     return
        res=client.groupAdd(UserGroup)
        _, img_encode = cv2.imencode('.jpg', self.show)
        img_base64 = base64.b64encode(img_encode.tobytes())
        result=client.addUser(str(img_base64,'utf-8'),'BASE64',UserGroup,EnglishName)
        if result['error_code']==0:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.namelist[EnglishName] = [EnglishName, ChineseName, UserGroup,result['result']['face_token']]
            self.label_13.setText("注册成功")
            with open("userdata.dat",'w') as userdata:
                for i in self.namelist.keys():
                    userdata.writelines(self.namelist[i][0]+','+self.namelist[i][1]+','+self.namelist[i][2]+','+self.namelist[i][3]+'\n')
            userdata.close()
        else:
            self.label_13.setText("注册失败")

    def faceUpdate(self):
        EnglishName=self.lineEdit_5.text()
        ChineseName=self.lineEdit_6.text()
        UserGroup=self.lineEdit_4.text()
        if not (EnglishName in self.namelist):
            self.label_14.setText('此人无数据')
            return
        if EnglishName== '' or ChineseName=='' or UserGroup=='':
            self.label_14.setText("信息为空！")
            return
        if self.flag==0:
            self.label_14.setText('未拍照备份')
            return
        # gray = cv2.cvtColor(self.show, cv2.COLOR_BGR2GRAY)
        # faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)
        # if len(faces)==0:
        #     self.label_14.setText("图片无人脸")
        #     return
        _, img_encode = cv2.imencode('.jpg', self.show)
        img_base64 = base64.b64encode(img_encode.tobytes())
        if self.namelist[EnglishName][2]==UserGroup:
            result=client.updateUser(str(img_base64,'utf-8'),'BASE64',UserGroup,EnglishName)
            if result['error_code']==0:
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_6.setText('')
                self.namelist[EnglishName] = [EnglishName, ChineseName, UserGroup,result['result']['face_token']]
                self.label_14.setText("更新成功")
                with open("userdata.dat",'w') as userdata:
                    for i in self.namelist.keys():
                        userdata.writelines(self.namelist[i][0]+','+self.namelist[i][1]+','+self.namelist[i][2]+','+self.namelist[i][3]+'\n')
                userdata.close()
            else:
                self.label_14.setText("更新失败")
        else:
            self.label_14.setText("与原用户组冲突")


    def faceDeletion(self):
        EnglishName=self.lineEdit_8.text()
        ChineseName=self.lineEdit_9.text()
        UserGroup=self.lineEdit_7.text()
        if (EnglishName in self.namelist)==False:
            self.label_15.setText('此人无数据')
            print(EnglishName)
            return
        if EnglishName== '' or ChineseName=='' or UserGroup=='':
            self.label_15.setText("信息为空！")
            return
        if self.namelist[EnglishName][2] == UserGroup:
            result = client.deleteUser(UserGroup,EnglishName)
            if result['error_code']==0:
                self.lineEdit_7.setText('')
                self.lineEdit_8.setText('')
                self.lineEdit_9.setText('')
                del self.namelist[EnglishName]
                self.label_15.setText('删除成功')
                with open("userdata.dat",'w') as userdata:
                    for i in self.namelist.keys():
                        userdata.writelines(self.namelist[i][0]+','+self.namelist[i][1]+','+self.namelist[i][2]+','+self.namelist[i][3]+'\n')
                userdata.close()
            else:
                self.label_15.setText('删除失败')
        else:
            self.label_15.setText('该用户组无此人')


    def LoadData(self):
        self.namelist={}
        try:
            userdata=open("userdata.dat", 'r')
        except:
            return
        else:
            tempdata=userdata.readlines()
            userdata.close()
        if tempdata==[] or tempdata[0]=='/n':
            return
        for temp in tempdata:
            temp=temp.split(',')
            temp[3]=temp[3][:len(temp[3])-1]
            self.namelist[temp[0]]=[temp[0],temp[1],temp[2],temp[3]]


#连接百度云
APP_ID='32021966'
API_KEY='qC7hU9AI5M8XfeZf1SxayBcx'
SECRET_KEY='mzNx2DMg1BnsebGzFpN06Y9kksnMGN6a'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def dis_img(image):
    # BGR => RGB 文件格式
    shrink = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # cv 图片转换成 qt图片
    qt_img =QtGui.QImage(shrink.data, shrink.shape[1],shrink.shape[0],shrink.shape[1] * 3,QtGui.QImage.Format_RGB888)
    return qt_img

def chineseText(image,text,px,py):
    font_size = 30
    py-=font_size
    font_color = (0, 0, 255)
    font_path = 'simhei.ttf' # 字体文件路径
    font = ImageFont.truetype(font_path, font_size)
    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    draw.text((px,py), text, font=font, fill=font_color)
    cv2_img = cv2.cvtColor(numpy.array(pil_img), cv2.COLOR_RGB2BGR)
    return  cv2_img

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =QtWidgets.QMainWindow()
    ui = Ui_mainForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())