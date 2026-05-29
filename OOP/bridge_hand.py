from collections import namedtuple
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError
        elif len(cards) != 13 or not all(isinstance(card, Card) for card in cards):
            raise ValueError
        
        self.cards = cards

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        parts = []
        for suit in Suit:
            cards_in_suit = sorted(
                [card for card in self.cards if card.suit == suit],
                key=lambda card: card.rank.value,
            )
            if cards_in_suit:
                ranks = "".join(card.rank.name for card in cards_in_suit)
                parts.append(f"{suit.name}:{ranks}")
        return " ".join(parts)
        

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        return sum(HCP.get(card.rank, 0) for card in self.cards)
    
    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        num = 0
        for suit in Suit:
            cards_in_suit = [card for card in self.cards if card.suit == suit]
            if len(cards_in_suit) == 2:
                num += 1
        return num

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        num = 0
        for suit in Suit:
            cards_in_suit = [card for card in self.cards if card.suit == suit]
            if len(cards_in_suit) == 1: 
                num += 1
        return num

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        num = 0
        for suit in Suit:
            cards_in_suit = [card for card in self.cards if card.suit == suit]
            if len(cards_in_suit) == 0: 
                num += 1
        return num

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        # doubletons = self.doubletons
        # singletons = self.singletons
        # voids = self.voids
        # return doubletons * 1 + singletons * 2 + voids * 3
        return sum(SSP.get(len([card for card in self.cards if card.suit == suit]), 0) for suit in Suit)


    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        losing_trick = 0
        for suit in Suit:
            top_3 = sorted(
                [card for card in self.cards if card.suit == suit],
                key=lambda card: card.rank.value,
            )[:3]
            ranks = {card.rank for card in top_3}
            safe_honors = 0

            if Rank.A in ranks:
                safe_honors += 1
            if len(top_3) >= 2 and Rank.K in ranks:
                safe_honors += 1
            if len(top_3) >= 3 and Rank.Q in ranks:
                safe_honors += 1

            losing_trick += len(top_3) - safe_honors
        return losing_trick



