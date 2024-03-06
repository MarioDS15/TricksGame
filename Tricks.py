from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
from Shuffle import create_deck, shuffle_deck, deal  # Adjusted import
from Card import Card  
from PyQt5.QtCore import Qt

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
            playerLayout = QHBoxLayout() if i % 2 == 0 else QVBoxLayout()
            playerLayout.setSpacing(-100)  # Adjust spacing for overlap. Make this more negative to increase overlap.

            for card in hand:
                card_ui = Card(card.suit, card.value)
                card_ui.setRotation(rotations[i])  # Set the rotation for the player's cards
                card_ui.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # Ensure all cards align consistently
                playerLayout.addWidget(card_ui)
                # Ensure cards are stacked correctly by adjusting the Z-order
                if playerLayout.count() > 1:
                    card_ui.stackUnder(playerLayout.itemAt(playerLayout.count() - 2).widget())

            row, col = positions[i]
            mainLayout.addLayout(playerLayout, row, col, alignment=Qt.AlignCenter)

        self.setLayout(mainLayout)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tricks()
    ex.show()
    sys.exit(app.exec_())
