# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'source/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 491)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStatusTip("")
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setToolTip("")
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button_layout = QtWidgets.QVBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.button_layout.addWidget(self.label)
        self.solutions_Button = QtWidgets.QPushButton(self.centralwidget)
        self.solutions_Button.setObjectName("solutions_Button")
        self.button_layout.addWidget(self.solutions_Button)
        self.gridLayout.addLayout(self.button_layout, 1, 4, 1, 1)
        self.error_Layout = QtWidgets.QVBoxLayout()
        self.error_Layout.setObjectName("error_Layout")
        self.error_input_Layout = QtWidgets.QFormLayout()
        self.error_input_Layout.setObjectName("error_input_Layout")
        self.n0_error_Label = QtWidgets.QLabel(self.centralwidget)
        self.n0_error_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.n0_error_Label.setObjectName("n0_error_Label")
        self.error_input_Layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.n0_error_Label)
        self.n0_error_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n0_error_Input.sizePolicy().hasHeightForWidth())
        self.n0_error_Input.setSizePolicy(sizePolicy)
        self.n0_error_Input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.n0_error_Input.setToolTip("")
        self.n0_error_Input.setObjectName("n0_error_Input")
        self.error_input_Layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.n0_error_Input)
        self.n_error_Label = QtWidgets.QLabel(self.centralwidget)
        self.n_error_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.n_error_Label.setObjectName("n_error_Label")
        self.error_input_Layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.n_error_Label)
        self.n_error_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_error_Input.sizePolicy().hasHeightForWidth())
        self.n_error_Input.setSizePolicy(sizePolicy)
        self.n_error_Input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.n_error_Input.setObjectName("n_error_Input")
        self.error_input_Layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.n_error_Input)
        self.error_Layout.addLayout(self.error_input_Layout)
        self.clear_error_Button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_error_Button.setObjectName("clear_error_Button")
        self.error_Layout.addWidget(self.clear_error_Button)
        self.gridLayout.addLayout(self.error_Layout, 1, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 3, 1, 1)
        self.input_Layout = QtWidgets.QGridLayout()
        self.input_Layout.setObjectName("input_Layout")
        self.clear_input_Button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_input_Button.setObjectName("clear_input_Button")
        self.input_Layout.addWidget(self.clear_input_Button, 2, 1, 1, 1)
        self.n_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_Input.sizePolicy().hasHeightForWidth())
        self.n_Input.setSizePolicy(sizePolicy)
        self.n_Input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.n_Input.setObjectName("n_Input")
        self.input_Layout.addWidget(self.n_Input, 1, 3, 1, 1)
        self.x_Label = QtWidgets.QLabel(self.centralwidget)
        self.x_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.x_Label.setObjectName("x_Label")
        self.input_Layout.addWidget(self.x_Label, 0, 2, 1, 1)
        self.reset_input_Button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_input_Button.setObjectName("reset_input_Button")
        self.input_Layout.addWidget(self.reset_input_Button, 2, 3, 1, 1)
        self.n_Label = QtWidgets.QLabel(self.centralwidget)
        self.n_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.n_Label.setObjectName("n_Label")
        self.input_Layout.addWidget(self.n_Label, 1, 2, 1, 1)
        self.y0_Label = QtWidgets.QLabel(self.centralwidget)
        self.y0_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.y0_Label.setObjectName("y0_Label")
        self.input_Layout.addWidget(self.y0_Label, 1, 0, 1, 1)
        self.y0_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y0_Input.sizePolicy().hasHeightForWidth())
        self.y0_Input.setSizePolicy(sizePolicy)
        self.y0_Input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.y0_Input.setObjectName("y0_Input")
        self.input_Layout.addWidget(self.y0_Input, 1, 1, 1, 1)
        self.x0_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x0_Input.sizePolicy().hasHeightForWidth())
        self.x0_Input.setSizePolicy(sizePolicy)
        self.x0_Input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.x0_Input.setObjectName("x0_Input")
        self.input_Layout.addWidget(self.x0_Input, 0, 1, 1, 1)
        self.x_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_Input.sizePolicy().hasHeightForWidth())
        self.x_Input.setSizePolicy(sizePolicy)
        self.x_Input.setMaximumSize(QtCore.QSize(75, 5555555))
        self.x_Input.setInputMask("")
        self.x_Input.setObjectName("x_Input")
        self.input_Layout.addWidget(self.x_Input, 0, 3, 1, 1)
        self.x0_Label = QtWidgets.QLabel(self.centralwidget)
        self.x0_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.x0_Label.setObjectName("x0_Label")
        self.input_Layout.addWidget(self.x0_Label, 0, 0, 1, 1)
        self.y_exact_Label = QtWidgets.QLabel(self.centralwidget)
        self.y_exact_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.y_exact_Label.setObjectName("y_exact_Label")
        self.input_Layout.addWidget(self.y_exact_Label, 1, 4, 1, 1)
        self.f_Label = QtWidgets.QLabel(self.centralwidget)
        self.f_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.f_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f_Label.setObjectName("f_Label")
        self.input_Layout.addWidget(self.f_Label, 0, 4, 1, 1)
        self.y_exact_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_exact_Input.sizePolicy().hasHeightForWidth())
        self.y_exact_Input.setSizePolicy(sizePolicy)
        self.y_exact_Input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.y_exact_Input.setObjectName("y_exact_Input")
        self.input_Layout.addWidget(self.y_exact_Input, 1, 5, 1, 1)
        self.f_Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_Input.sizePolicy().hasHeightForWidth())
        self.f_Input.setSizePolicy(sizePolicy)
        self.f_Input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.f_Input.setObjectName("f_Input")
        self.input_Layout.addWidget(self.f_Input, 0, 5, 1, 1)
        self.gridLayout.addLayout(self.input_Layout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.graph_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_widget.sizePolicy().hasHeightForWidth())
        self.graph_widget.setSizePolicy(sizePolicy)
        self.graph_widget.setObjectName("graph_widget")
        self.gridLayout.addWidget(self.graph_widget, 0, 0, 1, 4)
        self.checkbox_Layout = QtWidgets.QVBoxLayout()
        self.checkbox_Layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.checkbox_Layout.setObjectName("checkbox_Layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.checkbox_Layout.addItem(spacerItem)
        self.gridLayout.addLayout(self.checkbox_Layout, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.clear_input_Button.clicked.connect(self.n_Input.clear)
        self.clear_input_Button.clicked.connect(self.x0_Input.clear)
        self.clear_input_Button.clicked.connect(self.y0_Input.clear)
        self.clear_input_Button.clicked.connect(self.x_Input.clear)
        self.clear_input_Button.clicked.connect(self.y_exact_Input.clear)
        self.clear_input_Button.clicked.connect(self.f_Input.clear)
        self.clear_error_Button.clicked.connect(self.n0_error_Input.clear)
        self.clear_error_Button.clicked.connect(self.n_error_Input.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.x0_Input, self.y0_Input)
        MainWindow.setTabOrder(self.y0_Input, self.n_Input)
        MainWindow.setTabOrder(self.n_Input, self.x_Input)
        MainWindow.setTabOrder(self.x_Input, self.f_Input)
        MainWindow.setTabOrder(self.f_Input, self.y_exact_Input)
        MainWindow.setTabOrder(self.y_exact_Input, self.n0_error_Input)
        MainWindow.setTabOrder(self.n0_error_Input, self.n_error_Input)
        MainWindow.setTabOrder(self.n_error_Input, self.solutions_Button)
        MainWindow.setTabOrder(self.solutions_Button, self.clear_error_Button)
        MainWindow.setTabOrder(self.clear_error_Button, self.clear_input_Button)
        MainWindow.setTabOrder(self.clear_input_Button, self.reset_input_Button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DE Computational Assignment"))
        self.solutions_Button.setText(_translate("MainWindow", "Plot"))
        self.n0_error_Label.setText(_translate("MainWindow", "N<sub>0</sub>"))
        self.n0_error_Input.setText(_translate("MainWindow", "1"))
        self.n_error_Label.setText(_translate("MainWindow", "N<sub>1</sub>"))
        self.n_error_Input.setText(_translate("MainWindow", "10"))
        self.clear_error_Button.setToolTip(_translate("MainWindow", "Clear input fields"))
        self.clear_error_Button.setText(_translate("MainWindow", "Clear"))
        self.clear_input_Button.setToolTip(_translate("MainWindow", "Clear input fields"))
        self.clear_input_Button.setText(_translate("MainWindow", "Clear"))
        self.n_Input.setToolTip(_translate("MainWindow", "A positive integer"))
        self.n_Input.setText(_translate("MainWindow", "20"))
        self.x_Label.setText(_translate("MainWindow", "X"))
        self.reset_input_Button.setToolTip(_translate("MainWindow", "Reset input to default"))
        self.reset_input_Button.setText(_translate("MainWindow", "Reset"))
        self.n_Label.setText(_translate("MainWindow", "N"))
        self.y0_Label.setText(_translate("MainWindow", "y<sub>0</sub>"))
        self.y0_Input.setToolTip(_translate("MainWindow", "A rational number"))
        self.y0_Input.setText(_translate("MainWindow", "2"))
        self.x0_Input.setToolTip(_translate("MainWindow", "A rational number"))
        self.x0_Input.setText(_translate("MainWindow", "1"))
        self.x_Input.setToolTip(_translate("MainWindow", "A rational number greater than x<sub>0</sub>"))
        self.x_Input.setText(_translate("MainWindow", "6"))
        self.x0_Label.setText(_translate("MainWindow", "x<sub>0</sub>"))
        self.y_exact_Label.setText(_translate("MainWindow", "y(x,x<sub>0</sub>,y<sub>0</sub>)"))
        self.f_Label.setText(_translate("MainWindow", "f(x,y)"))
        self.y_exact_Input.setToolTip(_translate("MainWindow", "An exact solution with explicit const"))
        self.y_exact_Input.setText(_translate("MainWindow", "x * (exp(log(pow(y_0 / x_0 + 1, x / x_0))) - 1)"))
        self.f_Input.setToolTip(_translate("MainWindow", "A function for numerical calculations"))
        self.f_Input.setText(_translate("MainWindow", "(1 + y / x) * log(1 + y / x) + y / x"))
