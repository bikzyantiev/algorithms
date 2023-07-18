from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFileDialog, QTableWidget, QTableWidgetItem, QHBoxLayout, \
    QAbstractItemView, QMessageBox, QWidget, QListWidget
import resourses_rc
import back
class Ui_MainWindow(object):

    def slideLeftMenu(self):
        width = self.left_menu_container.width()
        print('hhh', width)
        newWidth = 140
        if width == 60:
            print(1)
            newWidth = 140
        elif width == 140:
            print(2)
            newWidth = 60
        h = 16777215
        self.anim_2 = QPropertyAnimation(self.left_menu_container, b"maximumSize")
        self.anim_2.setEndValue(QSize(newWidth, h))
        self.anim_2.setDuration(200)
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.anim_2.start()
    def listclicked1(self):
        g=[]
        print(f'clicked {tuple(self.list1.selectedItems()[0].text().split(", "))}')
        u=tuple(self.list1.selectedItems()[0].text().split(", "))
        r = back.tree_rules(self.pr)
        self.table_tree.setRowCount(0)
        self.table_tree.setRowCount(len(r[u]))
        for i in range(len(r[u])):
            self.table_tree.setItem(i, 0, QTableWidgetItem(f"{r[u][i][0]}"))
            self.table_tree.setItem(i, 1, QTableWidgetItem(f"{r[u][i][1]}"))
            self.table_tree.setItem(i, 2, QTableWidgetItem(f"{r[u][i][2]}"))
            self.table_tree.setItem(i, 3, QTableWidgetItem(f"{r[u][i][3]}"))
    def listclicked(self):
        g=[]
        for i in range(len(self.list.selectedItems())):
            g.append(self.list.selectedItems()[i].text())
        print(f'clicked {g}')
        r=back.what_if(self.o12, g, self.file, self.minp, self.maxp, self.mind, self.maxd)
        self.table_what.setRowCount(0)
        self.table_what.setRowCount(len(r))
        for i in range(len(r)):
            p=''
            for j in r[i]['r2']:
                p=p+j+', '
            p=p[:-2]

            self.table_what.setItem(i, 0, QTableWidgetItem(f"{p}"))
            self.table_what.setItem(i, 1, QTableWidgetItem(f"{r[i]['p']}"))
            self.table_what.setItem(i, 2, QTableWidgetItem(f"{r[i]['col']}"))
            self.table_what.setItem(i, 3, QTableWidgetItem(f"{r[i]['d']}"))
            self.table_what.setItem(i, 4, QTableWidgetItem(f"{r[i]['lift']}"))
    def close_sub_menu(self):  # ---------------------------------------
        width = self.widget.width()
        print(width)
        newWidth = 262
        if width == 262:
            print(1)
            newWidth = 1
        elif width == 1:
            print(2)
            newWidth = 262
        h = 16777215
        self.anim_2 = QPropertyAnimation(self.widget, b"maximumSize")
        self.anim_2.setEndValue(QSize(newWidth, h))
        self.anim_2.setDuration(250)
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.anim_2.start()

    global l,s
    l=0
    def open_file(self):
        global s
        s = QFileDialog.getOpenFileName()[0]
        self.alph=[]

        print(self.alph)
        self.lineEdit.setText(s)


    def table_(self):
        try:
            print(s)
            global fi
            fi=back.file1(s)
            self.file = back.file(s)

            self.tableWidget.setHorizontalHeaderLabels(fi[0])
            self.tableWidget.verticalHeader().setMinimumSectionSize(int((self.tab.height() / (len(fi))/len(fi))))
            self.tableWidget.setRowCount(len(fi) - 1)
            for i in range(1,len(fi)):
                self.tableWidget.setItem(i-1, 0, QTableWidgetItem(f"{fi[i][0]}"))
                self.tableWidget.setItem(i-1, 1, QTableWidgetItem(f"{fi[i][1]}"))

            for i in self.file:
                for j in (i.split(', ')):
                    if j not in self.alph:
                        self.alph.append(j)
            self.lineEdit.setText('')
            self.anim_2.setEndValue(QSize(0, 16777215))
            self.anim_2.setDuration(250)
            self.anim_2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.anim_2.start()
        except:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(6)
            self.tableWidget.verticalHeader().setMinimumSectionSize(int(self.tab.height() / 6))
            self.tableWidget.setHorizontalHeaderLabels(["Header 1", "Header 2"])
            QMessageBox.critical(self.tab, "Ошибка ", "Файл не соответсвует нужному формату\nПример заполнения можно посмотреть во вкладке 'help'", QMessageBox.Ok)
            self.lineEdit.setText('')
    def minimize_wind(self,MainWindow):
        MainWindow.setWindowState(MainWindow.windowState() | Qt.WindowMinimized)

    def open_full_screen_wind(self, MainWindow):
        global l
        if l==0:
            MainWindow.showFullScreen()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.full_screen_window.setIcon(icon)
            print(self.tableWidget.horizontalHeaderItem(0).text())
            if self.tableWidget.horizontalHeaderItem(0).text()=='Header 1':
                self.tableWidget.verticalHeader().setMinimumSectionSize(int(self.tab.height() / 6))
            else:
                self.tableWidget.verticalHeader().setMinimumSectionSize(int((self.tab.height() / len(fi))/len(fi)))
            if self.checkBox_3.checkState() == 2:
                self.table_what.horizontalHeader().setDefaultSectionSize(280)
            if self.checkBox_4.checkState() == 2:
                self.table_rules.horizontalHeader().setDefaultSectionSize(240)
            l=1
        elif l==1:
            MainWindow.showNormal()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.full_screen_window.setIcon(icon)
            if self.tableWidget.horizontalHeaderItem(0).text()=='Header 1':
                self.tableWidget.verticalHeader().setMinimumSectionSize(int(self.tab.height() / 6))
            else:
                self.tableWidget.verticalHeader().setMinimumSectionSize(int((self.tab.height() / (len(fi))/len(fi))))
            if self.checkBox_3.checkState() == 2:
                self.table_what.horizontalHeader().setDefaultSectionSize(128)
            if self.checkBox_4.checkState() == 2:
                self.table_rules.horizontalHeader().setDefaultSectionSize(150)
            l=0
    def close_wind(self, MainWindow):
        MainWindow.close()
    def menu(self, k):
        global k1
        h = 16777215
        width = self.stackedWidget.width()
        self.anim_2 = QPropertyAnimation(self.widget, b"maximumSize")
        self.anim_2.setEndValue(QSize(262, h))
        self.anim_2.setDuration(250)
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.anim_2.start()
        if width > 0 and k1 == k:
            self.anim_2.setEndValue(QSize(0, h))
            k1 = 0
        if k != 5:
            self.stackedWidget.setCurrentIndex(k)
            k1 = k
        else:
            self.anim_2.setEndValue(QSize(0, h))

    def as_rules(self):

        print(self.tabWidget.count())
        if self.tableWidget.horizontalHeaderItem(0).text() == 'Header 1':
            QMessageBox.critical(self.tab, "Ошибка ", "файл не загружен", QMessageBox.Ok)
        else:
            self.minp= int(self.spinBox_2.text())
            self.maxp = int(self.spinBox_4.text())

            self.mind = int(self.spinBox.text())
            self.maxd = int(self.spinBox_3.text())
            self.o12 = back.popul(self.file, self.minp, self.maxp)
            while self.tabWidget.count() != 1:
                self.tabWidget.removeTab(1)
            if self.checkBox_5.checkState() == 2:
                self.pop_sets = QtWidgets.QWidget()
                self.tabWidget.addTab(self.pop_sets, 'popular sets')
                self.table_pop_sets = QTableWidget(self.pop_sets)
                self.table_pop_sets.setObjectName(u"table_rules")
                self.horizontalLayout_15 = QHBoxLayout(self.pop_sets)
                self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
                self.horizontalLayout_15.addWidget(self.table_pop_sets)
                self.table_pop_sets.setStyleSheet("background-color: rgb(f, f, f);\n"
                                               "color:#000000;\n"
                                               "")

                self.table_pop_sets.setEditTriggers(QAbstractItemView.NoEditTriggers)
                self.table_pop_sets.setSelectionMode(QAbstractItemView.NoSelection)
                self.table_pop_sets.horizontalHeader().setHighlightSections(True)
                self.table_pop_sets.horizontalHeader().setProperty("showSortIndicator", False)
                self.table_pop_sets.horizontalHeader().setStretchLastSection(True)
                self.table_pop_sets.verticalHeader().setHighlightSections(True)
                self.table_pop_sets.verticalHeader().setProperty("showSortIndicator", False)
                self.table_pop_sets.verticalHeader().setStretchLastSection(True)

                self.table_pop_sets.setColumnCount(4)
                self.table_pop_sets.setRowCount(6)
                self.table_pop_sets.verticalHeader().setVisible(False)

                self.table_pop_sets.setHorizontalHeaderLabels(
                    ["№", "elements", "support", "col"])
                print(self.centralwidget.width())
                if self.centralwidget.width() < 1400:
                    print(1)
                    self.table_pop_sets.horizontalHeader().setDefaultSectionSize(150)
                else:
                    self.table_pop_sets.horizontalHeader().setDefaultSectionSize(240)
                p = self.o12
                self.table_pop_sets.setRowCount(len(p))
                for i in range(len(p)):
                    self.table_pop_sets.setItem(i, 0, QTableWidgetItem(f"{i + 1}"))
                    sl=''
                    for j in p[i]['line']:
                        sl = sl + j + ', '
                    sl = sl[:-2]
                    self.table_pop_sets.setItem(i, 1, QTableWidgetItem(f"{sl}"))
                    self.table_pop_sets.setItem(i, 2, QTableWidgetItem(f"{p[i]['p']}"))
                    self.table_pop_sets.setItem(i, 3, QTableWidgetItem(f"{p[i]['col']}"))
            if self.checkBox_4.checkState() == 2:
                self.rules = QtWidgets.QWidget()
                self.tabWidget.addTab(self.rules, 'rules')
                self.table_rules = QTableWidget(self.rules)
                self.table_rules.setObjectName(u"table_rules")
                self.horizontalLayout_15 = QHBoxLayout(self.rules)
                self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
                self.horizontalLayout_15.addWidget(self.table_rules)
                self.table_rules.setStyleSheet("background-color: rgb(f, f, f);\n"
                                               "color:#000000;\n"
                                               "")

                self.table_rules.setEditTriggers(QAbstractItemView.NoEditTriggers)
                self.table_rules.setSelectionMode(QAbstractItemView.NoSelection)
                self.table_rules.horizontalHeader().setHighlightSections(True)
                self.table_rules.horizontalHeader().setProperty("showSortIndicator", False)
                self.table_rules.horizontalHeader().setStretchLastSection(True)
                self.table_rules.verticalHeader().setHighlightSections(True)
                self.table_rules.verticalHeader().setProperty("showSortIndicator", False)
                self.table_rules.verticalHeader().setStretchLastSection(True)

                self.table_rules.setColumnCount(7)
                self.table_rules.setRowCount(6)
                self.table_rules.verticalHeader().setVisible(False)

                self.table_rules.setHorizontalHeaderLabels(["№", "condition","consequence","support","col","reliability","Lift"])
                print(self.centralwidget.width())
                if self.centralwidget.width()<1400:
                    print(1)
                    self.table_rules.horizontalHeader().setDefaultSectionSize(150)
                else:
                    self.table_rules.horizontalHeader().setDefaultSectionSize(240)
                p=back.rules(self.o12,self.file,self.minp, self.maxp, self.mind, self.maxd)
                self.table_rules.setRowCount(len(p))
                for i in range(len(p)):
                    self.table_rules.setItem(i, 0, QTableWidgetItem(f"{i+1}"))
                    ys = ''
                    for j in p[i]['r1']:
                        ys = ys + j + ', '
                    ys = ys[:-2]
                    self.table_rules.setItem(i, 1, QTableWidgetItem(f"{ys}"))
                    sl = ''
                    for j in p[i]['r2']:
                        sl = sl + j + ', '
                    sl = sl[:-2]
                    self.table_rules.setItem(i, 2, QTableWidgetItem(f"{sl}"))
                    self.table_rules.setItem(i, 3, QTableWidgetItem(f"{p[i]['p']}"))
                    self.table_rules.setItem(i, 4, QTableWidgetItem(f"{p[i]['c']}"))
                    self.table_rules.setItem(i, 5, QTableWidgetItem(f"{p[i]['d']}"))
                    self.table_rules.setItem(i, 6, QTableWidgetItem(f"{p[i]['lift']}"))
            if self.checkBox_2.checkState() == 2:
                self.tree_rules = QtWidgets.QWidget()
                self.tabWidget.addTab(self.tree_rules, 'tree rules')
                #
                self.horizontalLayout_12 = QHBoxLayout(self.tree_rules)
                self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
                self.list1 = QListWidget(self.tree_rules)
                self.list1.setObjectName(u"list")
                self.list1.setMaximumSize(QSize(500, 16777215))
                self.list1.setInputMethodHints(Qt.ImhMultiLine)
                self.horizontalLayout_12.addWidget(self.list1)
                self.pr = back.rules(self.o12, self.file, self.minp, self.maxp, self.mind, self.maxd)
                self.pr1=back.tree_rules(self.pr)
                l1=[]
                for t in self.pr1:
                    o=''
                    for t1 in t:
                       o=o+t1+', '
                    o=o[:-2]
                    l1.append(o)
                self.list1.addItems(l1)
                self.list1.itemClicked.connect(self.listclicked1)
                self.list1.setSelectionMode(QAbstractItemView.SingleSelection)
                self.table_tree = QTableWidget(self.tree_rules)
                self.table_tree.setStyleSheet(u"background-color: rgb(f, f, f);\n"
                                              "color:#000000;")
                self.table_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
                self.table_tree.setSelectionMode(QAbstractItemView.NoSelection)
                self.table_tree.horizontalHeader().setHighlightSections(True)
                self.table_tree.horizontalHeader().setProperty("showSortIndicator", False)
                self.table_tree.horizontalHeader().setStretchLastSection(True)
                self.table_tree.horizontalHeader().setMinimumSectionSize(int(self.table_tree.width() / 2))

                self.table_tree.verticalHeader().setHighlightSections(True)
                self.table_tree.verticalHeader().setProperty("showSortIndicator", False)
                self.table_tree.verticalHeader().setStretchLastSection(True)
                self.table_tree.verticalHeader().setMinimumSectionSize(int(self.table_tree.height() / 4))

                self.table_tree.setColumnCount(4)
                self.table_tree.setRowCount(6)
                self.table_tree.verticalHeader().setVisible(False)
                self.table_tree.setHorizontalHeaderLabels(["Rules", "Support", "reliability", "Lift"])
                self.horizontalLayout_12.addWidget(self.table_tree)
            if self.checkBox_3.checkState() == 2:
                self.what_if = QtWidgets.QWidget()
                self.what_if.setObjectName("what_if")
                self.tabWidget.addTab(self.what_if, "what if")
                #
                self.horizontalLayout_12 = QHBoxLayout(self.what_if)
                self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
                self.list = QListWidget(self.what_if)
                self.list.setObjectName(u"list")
                self.list.setMaximumSize(QSize(194, 16777215))
                self.list.setInputMethodHints(Qt.ImhMultiLine)
                self.horizontalLayout_12.addWidget(self.list)
                print(self.alph)
                self.list.addItems(self.alph)
                self.list.itemClicked.connect(self.listclicked)
                self.list.setSelectionMode(QAbstractItemView.MultiSelection)
                self.table_what = QTableWidget(self.what_if)
                self.table_what.setStyleSheet(u"background-color: rgb(f, f, f);\n"
                                              "color:#000000;")
                self.table_what.setEditTriggers(QAbstractItemView.NoEditTriggers)
                self.table_what.setSelectionMode(QAbstractItemView.NoSelection)
                self.table_what.horizontalHeader().setHighlightSections(True)
                self.table_what.horizontalHeader().setProperty("showSortIndicator", False)
                self.table_what.horizontalHeader().setStretchLastSection(True)
                self.table_what.horizontalHeader().setMinimumSectionSize(int(self.table_what.width() / 2))

                self.table_what.verticalHeader().setHighlightSections(True)
                self.table_what.verticalHeader().setProperty("showSortIndicator", False)
                self.table_what.verticalHeader().setStretchLastSection(True)
                self.table_what.verticalHeader().setMinimumSectionSize(int(self.table_what.height() / 5))

                self.table_what.setColumnCount(5)
                self.table_what.setRowCount(6)
                self.table_what.verticalHeader().setVisible(False)

                self.table_what.setHorizontalHeaderLabels(["Rules", "Support","col","reliability","Lift"])

                self.horizontalLayout_12.addWidget(self.table_what)
        self.anim_2.setEndValue(QSize(0, 16777215))
        self.anim_2.setDuration(250)
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.anim_2.start()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("*{\n"
                                 "    border:none;\n"
                                 "    background-color:transparent;\n"
                                 "    background:transparent;\n"
                                 "\n"
                                 "    padding:0;\n"
                                 "    margin:0;\n"
                                 "    color:#fff;\n"
                                 "}\n"
                                 "#centralwidget{\n"
                                 "    background-color: rgb(31, 35, 42);\n"
                                 "}\n"
                                 "\n"
                                 "#left_sub_menu_container{\n"
                                 "    background-color: rgb(22, 25, 29);\n"
                                 "}\n"
                                 "#left_sub_menu_container QPushButton{\n"
                                 "    text-align:left;\n"
                                 "    padding:2px 10px;\n"
                                 "    border-top-left-radius:10px;\n"
                                 "    border-bottom-left-radius:10px;\n"
                                 "}\n"
                                 "#frame_5{\n"
                                 "    background-color: rgb(22, 25, 29);\n"
                                 "    border-radius:10px\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.e = QtWidgets.QHBoxLayout(self.centralwidget)
        self.e.setContentsMargins(0, 0, 0, 0)
        self.e.setSpacing(10)
        self.e.setObjectName("e")
        self.left_menu_container = QtWidgets.QWidget(self.centralwidget)
        self.left_menu_container.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_menu_container.setMaximumSize(QSize(60, 16777215))
        self.left_menu_container.setObjectName("left_menu_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_menu_container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.left_sub_menu_container = QtWidgets.QWidget(self.left_menu_container)
        self.left_sub_menu_container.setObjectName("left_sub_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_sub_menu_container)
        self.verticalLayout_2.setContentsMargins(11, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_open = QtWidgets.QFrame(self.left_sub_menu_container)
        self.frame_open.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_open.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_open.setObjectName("frame_open")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_open)
        self.verticalLayout_3.setContentsMargins(0, 5, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.butt_open_menu = QtWidgets.QPushButton(self.frame_open)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.butt_open_menu.setFont(font)
        self.butt_open_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.butt_open_menu.setIcon(icon)
        self.butt_open_menu.setIconSize(QtCore.QSize(28, 28))
        self.butt_open_menu.setObjectName("butt_open_menu")

        self.verticalLayout_3.addWidget(self.butt_open_menu)
        self.verticalLayout_2.addWidget(self.frame_open)
        self.frame_home = QtWidgets.QFrame(self.left_sub_menu_container)
        self.frame_home.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.frame_home.setFont(font)
        self.frame_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_home.setLineWidth(2)
        self.frame_home.setObjectName("frame_home")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_home)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 11, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.butt_home = QtWidgets.QPushButton(self.frame_home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.butt_home.sizePolicy().hasHeightForWidth())
        self.butt_home.setSizePolicy(sizePolicy)
        self.butt_home.setMinimumSize(QtCore.QSize(0, 45))
        self.butt_home.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_home.setIcon(icon1)
        self.butt_home.setIconSize(QtCore.QSize(25, 25))
        self.butt_home.setObjectName("butt_home")
        self.verticalLayout_5.addWidget(self.butt_home)
        self.butt_file = QtWidgets.QPushButton(self.frame_home)
        self.butt_file.setMinimumSize(QtCore.QSize(0, 45))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_file.setIcon(icon2)
        self.butt_file.setIconSize(QtCore.QSize(25, 25))
        self.butt_file.setObjectName("butt_file")
        self.verticalLayout_5.addWidget(self.butt_file)
        self.butt_analyse = QtWidgets.QPushButton(self.frame_home)
        self.butt_analyse.setMinimumSize(QtCore.QSize(0, 45))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_analyse.setIcon(icon3)
        self.butt_analyse.setIconSize(QtCore.QSize(25, 25))
        self.butt_analyse.setObjectName("butt_analyse")
        self.verticalLayout_5.addWidget(self.butt_analyse)
        self.verticalLayout_2.addWidget(self.frame_home)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_help = QtWidgets.QFrame(self.left_sub_menu_container)
        self.frame_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_help.setObjectName("frame_help")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_help)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.butt_setting = QtWidgets.QPushButton(self.frame_help)
        self.butt_setting.setMinimumSize(QtCore.QSize(0, 35))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_setting.setIcon(icon4)
        self.butt_setting.setIconSize(QtCore.QSize(25, 25))
        self.butt_setting.setObjectName("butt_setting")
        self.verticalLayout_4.addWidget(self.butt_setting)
        self.butt_info = QtWidgets.QPushButton(self.frame_help)
        self.butt_info.setMinimumSize(QtCore.QSize(0, 35))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_info.setIcon(icon5)
        self.butt_info.setIconSize(QtCore.QSize(25, 25))
        self.butt_info.setObjectName("butt_info")
        self.verticalLayout_4.addWidget(self.butt_info)
        self.butt_help = QtWidgets.QPushButton(self.frame_help)
        self.butt_help.setMinimumSize(QtCore.QSize(0, 35))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_help.setIcon(icon6)
        self.butt_help.setIconSize(QtCore.QSize(25, 25))
        self.butt_help.setObjectName("butt_help")
        self.verticalLayout_4.addWidget(self.butt_help)
        self.verticalLayout_2.addWidget(self.frame_help)
        self.verticalLayout.addWidget(self.left_sub_menu_container)
        self.e.addWidget(self.left_menu_container)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(0,
                                                16777215))  # =------------------------------------------------------------------------------------------------------------------------------------
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 11, 8, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_9.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setStyleSheet("*{\n"
                                         "    background-color:rgb(22, 25, 29);\n"
                                         "    border-radius:10px\n"
                                         "}\n"
                                         "")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_file = QtWidgets.QWidget()
        self.page_file.setObjectName("page_file")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_file)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_4 = QtWidgets.QWidget(self.page_file)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(16, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file_path = QtWidgets.QFrame(self.widget_4)
        self.file_path.setStyleSheet("#file_path{\n"
                                     "    background-color: rgb(1, 25, 29);\n"
                                     "    border-radius:10px\n"
                                     "}\n"
                                     "#lineEdit{\n"
                                     "    background-color: rgb(31, 35, 42);\n"
                                     "    border-radius:5px\n"
                                     "}\n"
                                     "#butt_more{\n"
                                     "    background-color: rgb(31, 35, 42);\n"
                                     "    border-radius:5px\n"
                                     "}")
        self.file_path.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_path.setObjectName("file_path")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.file_path)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit = QtWidgets.QLineEdit(self.file_path)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.butt_more = QtWidgets.QPushButton(self.file_path)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(24)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.butt_more.sizePolicy().hasHeightForWidth())
        self.butt_more.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.butt_more.setFont(font)
        self.butt_more.setObjectName("butt_more")
        self.horizontalLayout_9.addWidget(self.butt_more)
        self.butt_go = QtWidgets.QPushButton(self.file_path)
        self.butt_go.setMinimumSize(QtCore.QSize(56, 24))
        self.butt_go.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "color:#000;")
        self.butt_go.setObjectName("butt_go")
        self.horizontalLayout_9.addWidget(self.butt_go)
        self.horizontalLayout_2.addWidget(self.file_path, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_8.addWidget(self.widget_4)
        self.stackedWidget.addWidget(self.page_file)
        self.page_analys = QtWidgets.QWidget()
        self.page_analys.setObjectName("page_analys")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_analys)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_9.setSpacing(36)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_5 = QtWidgets.QCheckBox(self.page_analys)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_9.addWidget(self.checkBox_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.page_analys)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_9.addWidget(self.checkBox_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_analys)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_9.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_analys)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_9.addWidget(self.checkBox_3)
        self.widget_5 = QtWidgets.QWidget(self.page_analys)
        self.widget_5.setStyleSheet("border:100;\n"
                                    "border-color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_5)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_11.addWidget(self.spinBox_2)
        self.spinBox_4 = QtWidgets.QSpinBox(self.widget_5)
        self.spinBox_4.setObjectName("spinBox_4")
        self.verticalLayout_11.addWidget(self.spinBox_4)
        self.verticalLayout_9.addWidget(self.widget_5)
        self.widget1 = QtWidgets.QWidget(self.page_analys)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_10.setContentsMargins(11, 11, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.widget1)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_10.addWidget(self.spinBox)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMaximum(100)
        self.spinBox_4.setMaximum(100)
        self.verticalLayout_10.addWidget(self.spinBox_3)
        self.verticalLayout_9.addWidget(self.widget1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.page_analys)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color:#000;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight)
        self.stackedWidget.addWidget(self.page_analys)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setObjectName("page_info")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_info)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page_info)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_info)
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setObjectName("page_settings")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_settings)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.page_settings)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_settings)
        self.page_help = QtWidgets.QWidget()
        self.page_help.setObjectName("page_help")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_help)
        self.horizontalLayout_6.setContentsMargins(-1, 25, -1, -1)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.page_help)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6, 0, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_help)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.e.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.right = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        self.right.setToolTipDuration(-1)
        self.right.setStyleSheet("")
        self.right.setObjectName("right")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.right)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.right)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_6 = QtWidgets.QFrame(self.widget_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.logo = QtWidgets.QLabel(self.frame_6)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/icons/icons/Group 1 (1).svg"))
        self.logo.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_10.addWidget(self.logo)
        self.logotext = QtWidgets.QLabel(self.frame_6)
        self.logotext.setObjectName("logotext")
        self.horizontalLayout_10.addWidget(self.logotext)
        self.horizontalLayout_8.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.widget_2)
        self.frame_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.butt_minimize_window = QtWidgets.QPushButton(self.frame_7)
        self.butt_minimize_window.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_minimize_window.setIcon(icon8)
        self.butt_minimize_window.setObjectName("butt_minimize_window")
        self.horizontalLayout_7.addWidget(self.butt_minimize_window)
        self.full_screen_window = QtWidgets.QPushButton(self.frame_7)
        self.full_screen_window.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.full_screen_window.setIcon(icon9)
        self.full_screen_window.setObjectName("full_screen_window")
        self.horizontalLayout_7.addWidget(self.full_screen_window)
        self.butt_close = QtWidgets.QPushButton(self.frame_7)
        self.butt_close.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butt_close.setIcon(icon10)
        self.butt_close.setIconSize(QtCore.QSize(25, 25))
        self.butt_close.setObjectName("butt_close")
        self.horizontalLayout_7.addWidget(self.butt_close)
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.verticalLayout_7.addWidget(self.widget_2, 0, QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.right)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_3)
        self.tabWidget.setStyleSheet("background-color: rgb(31, 35, 42);\n"
                                     "color:#fff;\n"
                                     "")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_7.addWidget(self.widget_3)
        self.e.addWidget(self.right)
        self.horizontalLayout_11 = QHBoxLayout(self.tab)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.horizontalLayout_11.addWidget(self.tableWidget)
        self.tableWidget.setStyleSheet("background-color: rgb(f, f, f);\n"
                                     "color:#000000;\n"
                                     "")

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(int(self.tab.width()/2))

        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(int(self.tab.height() / 5))
        self.tabWidget.setMovable(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(6)
        self.tableWidget.verticalHeader().setVisible(False)

        self.tableWidget.setHorizontalHeaderLabels(["Header 1", "Header 2"])
        # self.tableWidget.horizontalHeader().setSectionResizeMode(
        #     0, QtWidgets.QHeaderView.Fixed)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(
        #     1, QtWidgets.QHeaderView.Fixed)


        ########################--------------------------------------------------------------------------------------
        self.butt_open_menu.clicked.connect(self.slideLeftMenu)
        self.pushButton_9.clicked.connect(self.close_sub_menu)
        self.butt_file.clicked.connect(lambda: self.menu(0))
        self.butt_analyse.clicked.connect(lambda: self.menu(1))
        self.butt_setting.clicked.connect(lambda: self.menu(2))
        self.butt_info.clicked.connect(lambda: self.menu(3))
        self.butt_help.clicked.connect(lambda: self.menu(4))
        self.butt_home.clicked.connect(lambda: self.menu(5))
        self.butt_minimize_window.clicked.connect(lambda:self.minimize_wind(MainWindow))
        self.full_screen_window.clicked.connect(lambda: self.open_full_screen_wind(MainWindow))
        self.butt_close.clicked.connect(lambda: self.close_wind(MainWindow))
        self.butt_more.clicked.connect(self.open_file)
        self.butt_go.clicked.connect(self.table_)
        self.pushButton.clicked.connect(self.as_rules)
        ########################--------------------------------------------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.butt_home.setText(_translate("MainWindow", " Home"))
        self.butt_file.setText(_translate("MainWindow", " File"))
        self.butt_analyse.setText(_translate("MainWindow", " Data Analysis"))
        self.butt_setting.setText(_translate("MainWindow", " Settings"))
        self.butt_info.setText(_translate("MainWindow", " info"))
        self.butt_help.setText(_translate("MainWindow", " Help"))
        self.label.setText(_translate("MainWindow", "More Menu"))
        self.butt_more.setText(_translate("MainWindow", "..."))
        self.butt_go.setText(_translate("MainWindow", "import"))
        self.checkBox_5.setText(_translate("MainWindow", "popular sets"))
        self.checkBox_4.setText(_translate("MainWindow", "rules"))
        self.checkBox_2.setText(_translate("MainWindow", "tree-rules"))
        self.checkBox_3.setText(_translate("MainWindow", "what if"))
        self.label_3.setText(_translate("MainWindow", "support"))
        self.label_7.setText(_translate("MainWindow", "reliability"))
        self.pushButton.setText(_translate("MainWindow", "       ok       "))
        self.label_4.setText(_translate("MainWindow", "позже"))
        self.label_5.setText(_translate("MainWindow", "позже"))
        self.label_6.setText(_translate("MainWindow", "support: bikzyantiev@gmail.com"))
        self.logotext.setText(_translate("MainWindow", "CAP analys"))
        self.label_2.setText(_translate("MainWindow", u"version 1.0.1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "table"))


