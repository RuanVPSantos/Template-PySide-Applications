# Template App PySide6
1. Um sistema de rotas com um menu superior para alternar entre diferentes "abas".
2. Um menu completo.
3. Suporte para temas claro e escuro.
4. Estrutura modular e escalável para funções complexas, incluindo bancos de dados, APIs externas, etc.

### Estrutura de Pastas

```
my_pyside_app/
├── main.py
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── data.py
│   │   └── utils.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── dashboard.py
│   │   ├── settings.py
│   │   ├── report.py
│   │   ├── menu.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── api.py
│   └── styles/
│       ├── __init__.py
│       ├── style.qss
│       └── themes/
│           ├── light.qss
│           └── dark.qss
└── resources/
    ├── __init__.py
    └── data.csv
```

### Arquivos

#### main.py
```python
import sys
from PySide6.QtWidgets import QApplication
from app.gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```

#### README.md
```markdown
# My PySide Application

This is a sample application using PySide6 for GUI development.

## Installation

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On MacOS/Linux:
      ```sh
      source venv/bin/activate
      ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

```sh
python main.py
```
```

#### requirements.txt
```plaintext
PySide6==6.3.0
pandas==1.3.3
matplotlib==3.4.3
```

#### app/__init__.py
```python
# This file can be left empty or used for package initialization code
```

#### app/core/__init__.py
```python
# This file can be left empty or used for package initialization code
```

#### app/core/data.py
```python
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)
```

#### app/core/utils.py
```python
def format_date(date_str):
    return date_str.strftime('%Y-%m-%d')
```

#### app/gui/__init__.py
```python
# This file can be left empty or used for package initialization code
```

#### app/gui/main_window.py
```python
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton
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
```

#### app/gui/dashboard.py
```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from app.core.data import load_data

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)
        
        self.plot()
        
    def plot(self):
        data = load_data('resources/data.csv')
        ax = self.canvas.figure.subplots()
        ax.clear()
        data.plot(ax=ax)
        self.canvas.draw()
```

#### app/gui/settings.py
```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Configurações")
        layout.addWidget(label)
```

#### app/gui/report.py
```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ReportPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Relatórios")
        layout.addWidget(label)
```

#### app/gui/menu.py
```python
from PySide6.QtWidgets import QMenuBar, QMenu

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


```

#### app/services/__init__.py
```python
# This file can be left empty or used for package initialization code
```

#### app/services/database.py
```python
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

def query_db(query, args=(), one=False):
    conn = get_db_connection()
    cur = conn.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    conn.close()
    return (rv[0] if rv else None) if one else rv
```

#### app/services/api.py
```python
import requests

def get_data_from_api(url):
    response = requests.get(url)
    return response.json()
```

#### app/styles/__init__.py
```python
from .style import BUTTON_STYLE
```

#### app/styles/style.qss
```css
QPushButton {
    background-color: #4CAF50;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

QPushButton:hover {
    background-color: #45a049;
}
```

#### app/styles/themes/light.qss
```css
/* Light theme specific styles */
QMainWindow {
    background-color: white;
    color: black;
}
```

#### app/styles/themes/dark.qss
```css
/* Dark theme specific styles */
QMainWindow {
    background-color: #2B2B2B;
    color: white;
}
```

#### resources/__init__.py
```python
# This file can be left empty or used for package initialization code
```

#### resources/data.csv
```csv
date,value
2024-01-01,100
2024-01-02,110
2024-01-03,115
2024-01-04,120
2024-01-05,125
2024-01-06,130
2024-01-07,135
2024-01-08,140
2024-01-09,145
2024-01-10,150
```

### Scripts de Estilo em Python

#### app/styles/style.py
```python
BUTTON_STYLE = """
QPushButton {
    background-color: #4CAF50;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

QPushButton:hover {
    background-color: #45a049;
}
"""
```

### Executando a Aplicação

Para executar a aplicação, siga estas etapas:

1. **Criar um ambiente virtual**:
   ```sh
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No MacOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Instalar as dependências**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Executar a aplicação**:
   ```sh
   python main.py
   ```

Essa estrutura modulariza a aplicação, facilitando a manutenção e o crescimento do projeto. Cada módulo é responsável por uma parte específica da aplicação, tornando o código mais organizado e legível.