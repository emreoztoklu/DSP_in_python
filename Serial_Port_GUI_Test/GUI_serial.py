from PyQt5.QtWidgets import QTextEdit,QLineEdit,QPushButton,QWidget,QApplication,QMainWindow,QVBoxLayout,QHBoxLayout,QComboBox
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtCore import QIODevice

import sys

sc_size_width  = 1920
sc_size_height = 1080
win_size_width = 600
win_size_height = 200


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.listSerialPorts()

    
    def listSerialPorts(self):
        serialPortInfo = QSerialPortInfo()
        
        for serialPort in serialPortInfo.availablePorts():
            self.comboSerialPortList.addItem(serialPort.portName())

    def portConnect(self):
        self.serialPort.setPortName(self.comboSerialPortList.currentText())
        self.serialPort.setBaudRate(QSerialPort.Baud115200)
        self.serialPort.setDataBits(QSerialPort.Data8)
        self.serialPort.setParity(QSerialPort.NoParity)
        self.serialPort.setStopBits(QSerialPort.OneStop)
        
        if not self.serialPort.isOpen():
            self.serialPort.open(QIODevice.ReadWrite)  #yazma ve okuma modunda serial port açılışı
            self.pushButtonConnect.setEnabled(False)
            self.pushButtonDisConnect.setEnabled(True)
            self.pushButtonSend.setEnabled(True)
            
    def portDisConnect(self):        
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.pushButtonConnect.setEnabled(True)
            self.pushButtonDisConnect.setEnabled(False)
            self.pushButtonSend.setEnabled(False)
        
    def portSendData(self):
        self.serialPort.write(self.lineEditSendData.text().encode())
    
        
    def portDataReceived(self):
        
        for i in self.serialPort.readAll():
            if i == '\r':
               self.textEditReceivedData.append('\n') 
            
            self.textEditReceivedData.append(i)    
            print(i)
        
        
        
        'self.textEditReceivedData.append(self.serialPort.readAll().data().decode())'
    
    
    def initUI(self):
        self.serialPort = QSerialPort()
        self.setGeometry(sc_size_width/2 - win_size_width/2, sc_size_height/2- win_size_height/2, win_size_width, win_size_height)
        self.setWindowTitle("Serial Port GUI")
        ####################################### Combox oluşturma
        vboxana = QVBoxLayout()
        hbox1 = QHBoxLayout()
        self.comboSerialPortList = QComboBox()
        
        hbox1.addWidget(self.comboSerialPortList)
        ################################################### PushButton
        self.pushButtonConnect = QPushButton("Connect")
        self.pushButtonDisConnect = QPushButton("DisConnect!")
        self.pushButtonDisConnect.setEnabled(False)         #button transparan aktif değil
        hbox1.addWidget(self.pushButtonConnect)
        hbox1.addWidget(self.pushButtonDisConnect)
        ###################################################
        hbox1.addStretch()
        vboxana.addLayout(hbox1)
        #######################################
        hbox2=QHBoxLayout()
        ################################################### Text Edit
        self.textEditReceivedData = QTextEdit()
        self.textEditReceivedData.setFixedSize(300, 100)
        hbox2.addWidget(self.textEditReceivedData)
        
        ###################################################
        
        #######################################  
        vboxana.addLayout(hbox2)
        ################################################### Send Text
        hbox3 = QHBoxLayout()
        self.lineEditSendData = QLineEdit()
        self.pushButtonSend = QPushButton("Send")
        self.pushButtonSend.setEnabled(False)
        hbox3.addWidget(self.lineEditSendData)
        hbox3.addWidget(self.pushButtonSend)
        vboxana.addLayout(hbox3)
        
        ###################################################
        vboxana.addStretch()
        
        centralWidget = QWidget()
        centralWidget.setLayout(vboxana)
        
        self.setCentralWidget(centralWidget)
        #######################################
        
        self.pushButtonConnect.clicked.connect(self.portConnect)        
        self.pushButtonDisConnect.clicked.connect(self.portDisConnect)
        self.pushButtonSend.clicked.connect(self.portSendData)
        self.serialPort.readyRead.connect(self.portDataReceived)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())