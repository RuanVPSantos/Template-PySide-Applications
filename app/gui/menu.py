from PySide6.QtWidgets import QMenuBar, QMenu # type: ignore

class MenuBar(QMenuBar):
    def __init__(self, main_window):
        super().__init__()
        
        self.main_window = main_window
        
        file_menu = QMenu("Arquivo", self)
        view_menu = QMenu("Visualizar", self)
        help_menu = QMenu("Ajuda", self)
        
        file_menu.addAction("Abrir", self.on_open)
        file_menu.addAction("Salvar", self.on_save)
        file_menu.addSeparator()
        file_menu.addAction("Sair", self.on_quit)
        
        view_menu.addAction("Dashboard", self.on_dashboard)
        view_menu.addAction("Configurações", self.on_settings)
        view_menu.addAction("Relatórios", self.on_reports)
        
        self.addMenu(file_menu)
        self.addMenu(view_menu)
        self.addMenu(help_menu)
        
    def on_open(self):
        print("Abrir arquivo")
        
    def on_save(self):
        print("Salvar arquivo")
        
    def on_quit(self):
        print("Sair da aplicação")
        
    def on_dashboard(self):
        self.main_window.navigate_to(0)
        
    def on_settings(self):
        self.main_window.navigate_to(1)
        
    def on_reports(self):
        self.main_window.navigate_to(2)
