# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Back-stageManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_mainForm(object):
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
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 90, 141, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
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
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 90, 141, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 58, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 60, 51, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
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

        self.timer_camera = QtCore.QTimer()
        self.timer_camera.start(20)

        self.retranslateUi(mainForm)
        self.tabWidget.setCurrentIndex(2)
        self.pushButton.clicked.connect(self.takePicture) # type: ignore
        self.pushButton_2.clicked.connect(self.faceRegistration) # type: ignore
        self.pushButton_4.clicked.connect(self.faceUpdate) # type: ignore
        self.pushButton_5.clicked.connect(self.faceDeletion) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainForm)
        self.timer_camera.timeout.connect(self.show_camera)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "考勤机"))
        self.pushButton.setText(_translate("mainForm", "拍照备份"))
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =QtWidgets.QMainWindow()
    ui = Ui_mainForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())