import os

def load_styles(theme):
    base_path = os.path.dirname(os.path.abspath(__file__))
    theme_path = os.path.join(base_path, "themes", f"{theme}.qss")

    with open(theme_path, "r") as file:
        style = file.read()
    
    return style
