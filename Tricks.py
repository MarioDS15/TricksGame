from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
import Card

class CardGameUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Card Game with Rotated Cards')
        self.setGeometry(300, 300, 800, 600)

        # Main layout is a grid to place player hands on different edges
        mainLayout = QGridLayout(self)

        # Bottom player (no rotation needed)
        bottomLayout = QHBoxLayout()
        for _ in range(13):
            card = Card("Hearts", "Q")  # Example card
            bottomLayout.addWidget(card)
        mainLayout.addLayout(bottomLayout, 1, 0, 1, 1)

        # Right player (90 degrees rotation)
        rightLayout = QVBoxLayout()
        for _ in range(13):
            card = Card("Spades", "A")  # Example card
            card.setRotation(90)
            rightLayout.addWidget(card)
        mainLayout.addLayout(rightLayout, 0, 1, 1, 1)

        # Top player (180 degrees rotation)
        topLayout = QHBoxLayout()
        for _ in range(13):
            card = Card("Diamonds", "10")  # Example card
            card.setRotation(180)
            topLayout.addWidget(card)
        mainLayout.addLayout(topLayout, 0, 0, 1, 1)

        # Left player (270 degrees rotation)
        leftLayout = QVBoxLayout()
        for _ in range(13):
            card = Card("Clubs", "2")  # Example card
            card.setRotation(270)
            leftLayout.addWidget(card)
        mainLayout.addLayout(leftLayout, 0, 0, 1, 1)

        self.setLayout(mainLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CardGameUI()
    ex.show()
    sys.exit(app.exec_())
