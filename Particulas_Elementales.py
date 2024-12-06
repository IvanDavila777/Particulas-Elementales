#Particulas_Elementales.py
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from data import particles  # Importa la lista de partículas
import sys

class ParticleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Particulas Elementales")
        self.setGeometry(100, 100, 500, 300)
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()

        # Logo
        self.logo_label = QLabel(self)
        pixmap = QPixmap("test_logo.png")
        if pixmap.isNull():
            print("Error: No se pudo cargar la imagen 'test_logo.png'.")
            pixmap = QPixmap(200, 200)
            pixmap.fill(Qt.white)
        else:
            # Ajustar tamaño del logo
            pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_label)
        
        # Botón para mostrar la tabla de partículas
        self.show_table_button = QPushButton("Mostrar tabla de particulas elementales")
        self.show_table_button.clicked.connect(self.show_particles_table)
        layout.addWidget(self.show_table_button)

        # Campo de texto para buscar una partícula
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Ingresa el nombre de la particula para buscar...")
        layout.addWidget(self.search_input)

        # Botón para buscar la partícula
        self.search_button = QPushButton("Buscar particula")
        self.search_button.clicked.connect(self.search_particle)
        layout.addWidget(self.search_button)

        # Establecer el layout
        self.setLayout(layout)
    
    def show_particles_table(self):
        # Crear una nueva ventana para la tabla
        self.table_window = QWidget()
        self.table_window.setWindowTitle("Tabla de particulas elementales")
        self.table_window.setGeometry(200, 200, 600, 400)
        
        layout = QVBoxLayout()
        table = QTableWidget(len(particles), 7)  # 7 columnas: Name, Symbol, etc.
        table.setHorizontalHeaderLabels(["Name", "Symbol", "Type", "Family", "Mass", "Charge", "Spin"])
        
        # Poblar la tabla con datos de las partículas
        for row, particle in enumerate(particles):
            table.setItem(row, 0, QTableWidgetItem(particle.name))
            table.setItem(row, 1, QTableWidgetItem(particle.symbol))
            table.setItem(row, 2, QTableWidgetItem(particle.ptype))
            table.setItem(row, 3, QTableWidgetItem(particle.family))
            table.setItem(row, 4, QTableWidgetItem(f"{particle.mass:.2e}"))
            table.setItem(row, 5, QTableWidgetItem(str(particle.charge)))
            table.setItem(row, 6, QTableWidgetItem(str(particle.spin)))
        
        layout.addWidget(table)
        self.table_window.setLayout(layout)
        
        # Mostrar la ventana
        self.table_window.show()

    def search_particle(self):
        # Obtener el nombre de la partícula del campo de texto
        query = self.search_input.text().strip().lower()
        
        # Buscar la partícula en la lista
        result = next((p for p in particles if p.name.lower() == query), None)
        
        if result:
            # Si se encuentra la partícula, mostrar los detalles
            msg = f"Name: {result.name}\nSymbol: {result.symbol}\nType: {result.ptype}\nFamily: {result.family}\nMass: {result.mass:.2e}\nCharge: {result.charge}\nSpin: {result.spin}"
            QMessageBox.information(self, "Particula Encontrada", msg)
        else:
            # Si no se encuentra la partícula
            QMessageBox.warning(self, "Particula No Encontrada", "No se encontró ninguna partícula con ese nombre")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ParticleApp()
    main_window.show()
    sys.exit(app.exec_())
