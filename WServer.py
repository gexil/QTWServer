# -*- coding: iso-8859-1 -*-
"""
Created on Wed Apr 11 22:42:14 2018

@author: emmanuel
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from WServerUI import Ui_MainWindow
from server import TCPServer


class WServerForm(QMainWindow):
    
    
    
    def __init__(self, parent=None):
        super(WServerForm, self).__init__(parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        
        # un clic sur le bouton appellera la méthode 'action_bouton'
        self.ui.pushButton_StartStop.clicked.connect(self.action_start_stop)
        
        # on affiche un texte en bas de la fenêtre (status bar)
        self.ui.statusbar.showMessage("Hello")
        
        self.__port_number = 8080
        self.__started = False
        self.__server = None
    
    def action_start_stop(self):
        if(self.__started):
            self.__started = False
            self.__server.stop()
            self.ui.textEdit_Resume.insertPlainText("Server stop on port : "+str(self.__port_number)+"\n")
            self.ui.pushButton_StartStop.setText("Start")
            self.ui.lineEdit_portNumber.setEnabled(True)
            self.__server = None
            self.ui.lcdNumber_NbClients.display(0)
        else:
            self.__started = True
            self.__port_number = int(self.ui.lineEdit_portNumber.text())
            self.ui.pushButton_StartStop.setText("Stop")
            self.ui.lineEdit_portNumber.setEnabled(False)
            self.__server = TCPServer(('127.0.0.1',self.__port_number))
            self.__server.evt_server_clientConnected += self.onClientConnected
            self.__server.evt_server_clientDisconnected += self.onClientDiconnected
            self.__server.evt_server_clientReceive += self.onClientReceive
            self.ui.textEdit_Resume.insertPlainText("Server start on port : "+str(self.__port_number)+"\n")
            self.__server.start()
            
    
    def onClientConnected(self, sender, message):
        if (not (self.__server is None)):
            self.ui.textEdit_Resume.insertPlainText(message+"\n")
            self.ui.lcdNumber_NbClients.display(self.__server.numberOfConnexion)
        
    
    def onClientDiconnected(self, sender, message):
        if (not (self.__server is None)):
            self.ui.textEdit_Resume.insertPlainText(message+"\n")
            self.ui.lcdNumber_NbClients.display(self.__server.numberOfConnexion)
    
    def onClientReceive(self, sender, message):
        if (not (self.__server is None)):
            self.ui.textEdit_Resume.insertPlainText(message+"\n")
    

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    wserver = WServerForm()
    wserver.show()
    
sys.exit(app.exec_())