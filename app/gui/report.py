from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel # type: ignore

class ReportPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Relatórios")
        layout.addWidget(label)