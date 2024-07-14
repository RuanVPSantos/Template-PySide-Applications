from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton # type: ignore
from app.gui.dashboard import DashboardPage
from app.gui.settings import SettingsPage
from app.gui.report import ReportPage
from app.gui.menu import MenuBar
from app.styles import style

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicação com Sistema de Rotas e Menu")
        self.setGeometry(100, 100, 1200, 800)
        
        self.stacked_widget = QStackedWidget()
        
        self.dashboard_page = DashboardPage()
        self.settings_page = SettingsPage()
        self.report_page = ReportPage()
        
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.settings_page)
        self.stacked_widget.addWidget(self.report_page)
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)
        
        self.setStyleSheet(style.BUTTON_STYLE)
        
    def navigate_to(self, page_index):
        self.stacked_widget.setCurrentIndex(page_index)