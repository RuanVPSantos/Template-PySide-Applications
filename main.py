import sys
from PySide6.QtWidgets import QApplication # type: ignore
from app.gui.main_window import MainWindow
from app.styles import load_styles

def main():
    app = QApplication(sys.argv)

    # Carregar estilos QSS
    style = load_styles("dark")
    app.setStyleSheet(style)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
