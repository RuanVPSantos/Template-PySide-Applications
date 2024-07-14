from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication # type: ignore
from app.styles import load_styles

class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.light_theme_button = QPushButton("Tema Claro")
        self.dark_theme_button = QPushButton("Tema Escuro")
        
        self.light_theme_button.clicked.connect(self.set_light_theme)
        self.dark_theme_button.clicked.connect(self.set_dark_theme)
        
        self.layout.addWidget(self.light_theme_button)
        self.layout.addWidget(self.dark_theme_button)
        
    def set_light_theme(self):
        style = load_styles("light")
        QApplication.instance().setStyleSheet(style)
        
    def set_dark_theme(self):
        style = load_styles("dark")
        QApplication.instance().setStyleSheet(style)
