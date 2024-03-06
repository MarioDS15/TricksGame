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
        self.setFixedSize(60, 80)
        self.setStyleSheet("QLabel { background-color: blue; }")

    def updatePixmap(self):
        # Adjust the value for face cards and Ace
        value_str = {'11': 'J', '12': 'Q', '13': 'K', '14': 'A'}.get(str(self.value), str(self.value))
        #value_str = str(self.value).replace('10', 'T') 
        # Construct the file path for the card image
        image_path = f'images/cards/{self.value}_of_{self.suit}.png'
        
        # Load the image and set it as the pixmap for this label
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Failed to load image at {image_path}")
        else:
            print(f"Loaded image at {image_path}")
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def setRotation(self, angle):
        self.rotation = angle
        if self.pixmap():
            # Apply rotation
            transform = QTransform().rotate(self.rotation)
            rotated_pixmap = self.pixmap().transformed(transform, Qt.SmoothTransformation)
            self.setPixmap(rotated_pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def enterEvent(self, event):
        # Expand or show the card on hover
        self.setFixedSize(80, 100)

    def leaveEvent(self, event):
        # Return to the overlapped size
        self.setFixedSize(60, 80)

