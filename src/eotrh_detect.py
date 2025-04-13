import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QButtonGroup, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

# Global scoring variables
clinical_score = 0
radio_score = 0

# ───── INTERPRETATION ─────
def interpret_clinical(p):
    if p == 0:
        return "Clinical stage: 0", "No findings, healthy", "Score: 0", "Clinical normality. Subclinical involvement cannot be excluded."
    elif p <= 2:
        return "Clinical stage: 1", "Suspicious", "Score: 1-2", "Minimal clinical signs. May correspond to very early stages."
    elif p <= 5:
        return "Clinical stage: 2", "Mild", "Score: 3-5", "Presence of clear but localized clinical signs."
    elif p <= 9:
        return "Clinical stage: 3", "Moderate", "Score: 6-9", "Multiple clinical signs and medium intensity."
    else:
        return "Clinical stage: 4", "Severe", "Score: ≥10", "Generalized and severe clinical involvement."

def interpret_radio(p):
    if p == 0:
        return "Radiographic stage: 0", "Normal", "Score: 0", "No abnormal radiological findings. Does not exclude mild EOTRH."
    elif p <= 2:
        return "Radiographic stage: 1", "Suspicious", "Score: 1-2", "Tooth shape preserved but sporadic deviations: slightly blunted root tip, surface irregular/rough, slightly altered tooth structure"
    elif p <= 5:
        return "Radiographic stage: 2", "Mild", "Score: 3-5", "Tooth shape preserved, slightly blunted root tip, surface irregular/rough, slightly altered tooth structure"
    elif p <= 9:
        return "Radiographic stage: 3", "Moderate", "Score: 6-9", "Tooth shape largely preserved, intra-alveolar tooth part is not wider than the clinical crown, obviously blunted root tip, surface irregular/rough, moderately altered tooth structure"
    else:
        return "Radiographic stage: 4", "Severe", "Score: ≥10", "Loss of tooth shape, intra-alveolar tooth part is wider than the clinical crown, surface obviously irregular/rough, severely altered tooth structure. Coincides with severe clinical signs."

def interpret_final(p):
    if p <= 12:
        return "Low suspicion of EOTRH", "Insufficient clinical and radiographic evidence. Routine follow-up and examination recommended."
    elif p <= 25:
        return "Moderate suspicion of EOTRH", "Some signs compatible with EOTRH. Periodic follow-up recommended."
    elif p <= 34:
        return "High suspicion of EOTRH", "Clear coincidence between clinical and radiographic signs. Immediate evaluation required."
    else:
        return "Very high suspicion of severe EOTRH", "Strong and consistent indicators. Urgent therapeutic action recommended."

# ───── INTERFACE ─────
class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EOTRH Detect")
        self.setStyleSheet("background-color: #f0fef0;")
        layout = QVBoxLayout()

        title = QLabel("Welcome to EOTRH Detect: EOTRH diagnostic software")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #0A3D2E; font-family: Arial")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)


        img = QLabel()
        logo_pixmap = QPixmap("cavall.png").scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pix = QPixmap("cavall.png").scaledToWidth(300, Qt.SmoothTransformation)
        img.setPixmap(pix)
        img.setAlignment(Qt.AlignCenter)

        button = QPushButton("Start diagnosis")
        button.setStyleSheet("background-color: #8fc98f; font-size: 16px;")
        button.clicked.connect(self.start)

        layout.addWidget(title)
        layout.addWidget(img)
        layout.addWidget(button)
        # Footer message
        footer = QLabel("Version 1.0 · Developed by Martina · 2025")
        footer.setStyleSheet("font-size: 10px; color: #555")
        footer.setAlignment(Qt.AlignCenter)

        # Add it to the layout (after the button)
        layout.addWidget(footer)

        self.setLayout(layout)

    def start(self):
        self.clinical_window = ClinicalLayer()
        self.clinical_window.show()
        self.close()

class ClinicalLayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manual clinical signs layer")
        self.setStyleSheet("background-color: #f0fef0;")
        layout = QVBoxLayout()

        self.titles = [
            ("Fistulae", [("1 purulent or up to 3 serous", 1), ("2-3 purulent or 4-6 serous", 2), (">3 purulent or >6 serous", 3)]),
            ("Gingival recession", [("<1/3 of the root exposed", 1), ("<2/3 of root exposed", 2), ("Whole root exposed", 3)]),
            ("Subgingval bulbous enlargement", [("No", 0), ("Yes", 1)]),
            ("Gingivitis", [("Focal", 1), ("Widespread", 2), ("Blueish colour", 3)]),
            ("Bite angle", [("15 years old and pincer like", 1), ("Over 15 years old and bisection angle", 2), ("Over 15 years old and pincer like", 3)])
        ]

        self.button_questions = []
        self.groups = []

        for title, options in self.titles:
            layout.addWidget(QLabel(f"<b>{title}</b>", font=QFont('Arial', 14)))
            group = QButtonGroup(self)
            for text, value in options:
                rb = QRadioButton(text)
                rb.setProperty("value", value)
                group.addButton(rb)
                layout.addWidget(rb)
            self.groups.append(group)

        button = QPushButton("Next")
        button.setStyleSheet("background-color: #8fc98f; font-size: 16px;")
        button.clicked.connect(self.next)
        layout.addWidget(button)
        self.setLayout(layout)

    def next(self):
        global clinical_score
        clinical_score = 0
        for group in self.groups:
            selected_button = group.checkedButton()
            if selected_button:
                clinical_score += selected_button.property("value")

        self.info = QLabel("Switching to radiographic signs analysis...")
        self.info.setFont(QFont('Arial', 14))
        QMessageBox.information(self, "Information", "Now radiographic signs will be analyzed.")

        self.radio_window = RadiographicLayer()
        self.radio_window.show()
        self.close()

class RadiographicLayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manual radiographic layer")
        self.setStyleSheet("background-color: #f0fef0;")
        layout = QVBoxLayout()

        self.titles = [
            ("Quantity: Teeth Affected", [("0", 0), ("1-4", 1), ("5-8", 2), (">≤9", 3)]),
            ("Quantity: Missing/Extracted teeth", [("None", 0), ("One or more incisors already missing/extracted", 1)]),
            ("Tooth shape", [("Regular", 0), ("Preserved: slightly blunted root tip, enlargement of the periodontal space", 1), ("Largely preserved: circumferential increase of the root tip or the more occlusal part of the tooth, intra-alveolar tooth part < clinical crown", 2), ("Largely lost: intra-alveolar tooth part = clinical crown", 3), ("Lost: intra-alveolar tooth part > clinical crown", 4)]),
            ("Tooth structure", [("No radiological findings", 0), ("Mild: single area of increased radiolucency (up to max. 1/3 of the root width)", 1), ("Moderate: multiple areas of increased radiolucency (up to max. 1/3) or two (up to 2/3)", 2), ("Severe: large areas of increased radiolucency", 3)]),
            ("Tooth surface", [("No radiological findings", 0), ("1 irregularity (up to max 1/3 root length)", 1), ("2 irregularities / rough surface", 2), ("Obviously irregular (surface slumps)/ rough", 3)])
        ]

        self.groups = []
        for title, options in self.titles:
            layout.addWidget(QLabel(f"<b>{title}</b>", font=QFont('Arial', 14)))
            group = QButtonGroup(self)
            for text, value in options:
                rb = QRadioButton(text)
                rb.setProperty("value", value)
                group.addButton(rb)
                layout.addWidget(rb)
            self.groups.append(group)

        button = QPushButton("Show Results")
        button.setStyleSheet("background-color: #8fc98f; font-size: 16px;")
        button.clicked.connect(self.results)
        layout.addWidget(button)
        self.setLayout(layout)

    def results(self):
        global radio_score
        radio_score = 0
        for group in self.groups:
            selected_button = group.checkedButton()
            if selected_button:
                radio_score += selected_button.property("value")

        self.result_window = ResultWindow()
        self.result_window.show()
        self.close()

class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Final Result")
        self.setStyleSheet("background-color: #f0fef0;")
        layout = QVBoxLayout()

        total = clinical_score + radio_score
        c1, c2, c3, c4 = interpret_clinical(clinical_score)
        r1, r2, r3, r4 = interpret_radio(radio_score)
        f1, f2 = interpret_final(total)

        layout.addWidget(QLabel(f"<h2>Clinical results</h2>\nScore: {clinical_score}"))
        layout.addWidget(QLabel(f"{c1}\n{c2}\n{c3}\n{c4}"))
        layout.addWidget(QLabel(f"<h2>Radiographic results</h2>\nScore: {radio_score}"))
        layout.addWidget(QLabel(f"{r1}\n{r2}\n{r3}\n{r4}"))
        layout.addWidget(QLabel(f"<h2>Final classification</h2>\nTotal score: {total}/41\n{f1}\n{f2}"))

        self.setLayout(layout)

# ───── EXECUTION ─────
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec_())
