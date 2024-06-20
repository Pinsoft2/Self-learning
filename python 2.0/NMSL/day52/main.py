from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        #create widgets
        distance_label = QLabel("Distance:")
        self.distance_edit = QLineEdit()
        #here insert dropdown button
        self.unit_dropdown = QComboBox()
        self.unit_dropdown.addItem('Metric(km)')
        self.unit_dropdown.addItem('Imperial (miles)')

        time_label = QLabel("Time (hours):")
        self.time_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_edit, 0, 1)
        grid.addWidget(self.unit_dropdown, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        self.setLayout(grid)

    def calculate_speed(self):
        match self.unit_dropdown.currentText():
            case 'Metric(km)':
                speed = float(self.distance_edit.text()) / float(self.time_edit.text())
                self.output_label.setText(f"Average Speed: {round(speed, 2)} km/h" )
            case 'Imperial (miles)':
                speed = float(self.distance_edit.text()) / float(self.time_edit.text())
                self.output_label.setText(f"Average Speed: {round(speed, 2)} mph" )

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())