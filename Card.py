from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt

class Card(QLabel):
    def __init__(self, suit, value, parent=None):
        super(Card, self).__init__(parent)
        self.suit = suit.lower()
        self.value = value
        self.setRotation(0)  # Default rotation
        self.updatePixmap()
        self.setFixedSize(80, 112)

    def updatePixmap(self):
        # Adjust the value for face cards and Ace
        value_str = {
            '11': 'J', '12': 'Q', '13': 'K', '14': 'A'
        }.get(str(self.value), str(self.value))
        
        # Construct the file path for the card image
        image_path = f'images/{value_str}_of_{self.suit}.png'
        
        # Load the image and set it as the pixmap for this label
        pixmap = QPixmap(image_path).scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.setPixmap(pixmap)

    def enterEvent(self, event):
        # Expand or show the card on hover
        self.setFixedSize(100, 140)

    def leaveEvent(self, event):
        # Return to the overlapped size
        self.setFixedSize(80, 112)

    def setRotation(self, angle):
        self.rotation = angle
        if self.pixmap():
            transform = QTransform().rotate(self.rotation)
            rotatedPixmap = self.pixmap().transformed(transform, Qt.SmoothTransformation)
            self.setPixmap(rotatedPixmap)
        else:
            # If no pixmap is set, you can adjust the placeholder style
            self.setStyleSheet("QLabel { background-color: red; transform: rotate(%ddeg); }" % angle)

    def setRotation(self, angle):
        self.rotation = angle
        if self.pixmap():
            # Apply rotation
            transform = QTransform().rotate(self.rotation)
            rotatedPixmap = self.pixmap().transformed(transform, Qt.SmoothTransformation)
            self.setPixmap(rotatedPixmap)
