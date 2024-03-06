from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt

class Card(QLabel):
    def __init__(self, suit, value, parent=None):
        super(Card, self).__init__(parent)
        self.suit = suit
        self.value = value
        self.setRotation(0)  # Default rotation
        self.updatePixmap()

    def updatePixmap(self):
        # Placeholder for setting the card image based on suit and value
        # In a real application, you'd load an actual image
        pixmap = QPixmap(100, 140)
        pixmap.fill(Qt.transparent)  # Placeholder: make the pixmap transparent

        # Set the pixmap to the label
        self.setPixmap(pixmap)

    def setRotation(self, angle):
        self.rotation = angle
        if self.pixmap():
            # Apply rotation
            transform = QTransform().rotate(self.rotation)
            rotatedPixmap = self.pixmap().transformed(transform, Qt.SmoothTransformation)
            self.setPixmap(rotatedPixmap)
