from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
from Shuffle import create_deck, shuffle_deck, deal  # Adjusted import
from Card import Card  

class Tricks(QWidget):
    def __init__(self):
        super().__init__()
        self.deck = create_deck()  # Create a deck of cards
        self.shuffled_deck = shuffle_deck(self.deck)  # Shuffle the deck
        self.hands = deal(self.shuffled_deck)  # Deal the cards into 4 hands
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Card Game with Rotated Cards')
        self.setGeometry(300, 300, 800, 600)

        # Main layout is a grid to place player hands on different edges
        mainLayout = QGridLayout()

        # Setup the layouts for each player with their dealt hand
        positions = [(2, 1), (1, 2), (0, 1), (1, 0)]  # Grid positions for bottom, right, top, left
        rotations = [0, 90, 180, 270]  # Rotations for each player's cards
        for i, hand in enumerate(self.hands):
            playerLayout = QVBoxLayout() if i % 2 else QHBoxLayout()
            for card in hand:
                card_ui = Card(card.suit, card.value)  # Create a UI representation of the card
                card_ui.setRotation(rotations[i])  # Set rotation
                card_ui.setStyleSheet("border: 1px solid black;")  # Add border for debugging
                playerLayout.addWidget(card_ui)
            # Add the player's layout to the main grid layout
            row, col = positions[i]
            mainLayout.addLayout(playerLayout, row, col)

        self.setLayout(mainLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tricks()
    ex.show()
    sys.exit(app.exec_())
