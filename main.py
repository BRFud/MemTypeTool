import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from leftMenuClass import *
from credListClass import *
from credEditClass import *

class Window(QMainWindow):
    """This class creates a main window"""

    #Constructor
    def __init__(self):
        super().__init__() #Call super class constructor

        #Set Title
        self.setWindowTitle("MtTool - area0x33")

        #Create Top header
        self.topFont = QFont("Helvetica", 32, QFont.Bold)
        self.topPalette = QPalette()
        self.topPalette.setColor(QPalette.Foreground,Qt.white)
        self.topLayout = QHBoxLayout()
        self.topLabel = QLabel()
        self.topLabel.setText("MemType Tool")
        self.topLabel.setFont(self.topFont)
        self.topLabel.setPalette(self.topPalette)
        self.topLabel.setAlignment(Qt.AlignLeft)

        self.topLogo = QLabel()
        self.topLogo.setPixmap(QPixmap("img/logo.png"))
        self.topLogo.setAlignment(Qt.AlignRight)
        self.topLayout.addWidget(self.topLabel)
        self.topLayout.addWidget(self.topLogo)

        self.topWidget = QWidget()
        self.topWidget.setStyleSheet("background-color:darkgrey;")
        self.topWidget.setLayout(self.topLayout)

        #Create left main menu
        self.menu = leftMenu((("Read","img/read.png"),("Write","img/write.png"), ("Set PIN","img/pin.png"), ("Import File","img/open.png"), ("Export File","img/save.png"),("Set KeyLayout","img/keylayout.png")))

        self.menu.menuClicked.connect(self.menuClicked)
        #Create Center Layout
        self.centLayout = QVBoxLayout()
        self.centLayout.addWidget(self.menu)
        #TODO FORM TEST
       # self.centCredList = credList(("Gmail", "Skype", "Work Sftp1", "WrkLaptop", "WrkSkype", "WrkWebAdmin", "WrkServer1SSH"))
       # self.centLayout.addWidget(self.centCredList)
        self.centCredEdit = credEdit()
        self.centLayout.addWidget(self.centCredEdit)

        self.centCredEdit.okPressed.connect(self.printOk)
        self.centCredEdit.cancelPressed.connect(self.printCancel)


        #Create Main Layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.topWidget)
        self.mainLayout.addLayout(self.centLayout)


        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    def printOk(self):
        print("OK PRESSED!")

    def printCancel(self):
        print("CANCEL PRESSED!")

    def menuClicked(self,button):
        print("%s CLICKED" %(button))
        #Check what menu button was pressed!
        if(button == "Set Pin"):
            text, ok = QInputDialog.getText(self, 'Set new PIN','Enter new PIN:')
        elif(button == "Import File"):
            inFile = QFileDialog.getOpenFileName(self, 'Import File','./')
        elif(button == "Export File"):
            inFile = QFileDialog.getOpenFileName(self, 'Export File')
        elif(button == "Set KeyLayout"):
            inFile = QFileDialog.getOpenFileName(self, 'Choose KeyLayout')



def main():
    #Create new application
    mttool = QApplication(sys.argv)
    #Create new instance of main window
    mtWindow = Window()
    mtWindow.show() #Make instance visible
    mtWindow.raise_() #Raise instance to top of window stack
    mttool.exec_()

if __name__ == "__main__":
    main()