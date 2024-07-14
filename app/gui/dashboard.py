from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from app.core.data import load_data
import matplotlib.pyplot as plt

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.canvas = FigureCanvas(Figure(figsize=(5, 3), facecolor='#1a1b26'))
        layout.addWidget(self.canvas)
        
        self.apply_dark_theme()
        
        self.plot()
        
    def apply_dark_theme(self):
        plt.style.use('dark_background')
        plt.rcParams.update({
            "axes.facecolor": "#1a1b26",
            "figure.facecolor": "#1a1b26",
            "savefig.facecolor": "#1a1b26",
            "savefig.edgecolor": "#1a1b26",
            "figure.edgecolor": "#1a1b26",
            "axes.edgecolor": "#1a1b26",
            "grid.color": "#414868",
            "xtick.color": "#a9b1d6",
            "ytick.color": "#a9b1d6",
            "text.color": "#a9b1d6",
            "lines.color": "#a9b1d6",
            "patch.edgecolor": "#a9b1d6",
            "patch.facecolor": "#3b4261",
            "axes.edgecolor" : "#a9b1d6",
            "axes.prop_cycle": plt.cycler(color=["#7aa2f7", "#bb9af7", "#7dcfff", "#9ece6a", "#e0af68", "#f7768e", "#ff9e64"])
        })
        
    def plot(self):
        data = load_data('resources/data.csv')
        ax = self.canvas.figure.add_subplot(111)
        ax.clear()
        data.plot(ax=ax)
        self.canvas.draw()
