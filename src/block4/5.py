# from collections.abc import Iterator
from typing import List
import random


class CardDeck:
    __DECK_SIZE = 52
    __SUITS = ["Пик", "Черви", "Крести", "Бубны"]
    __RANKS = [str(i) for i in range(2, 11)] + [
        "Валет",
        "Дама",
        "Король",
        "Туз",
    ]

    def __shufle(self, deck: None | List[str] = None) -> List[str]:
        if deck is not None:
            updated = deck
            random.shuffle(updated)
            return updated
        new_deck = [
            f"{rank:<6} {suit}"
            for rank in self.__RANKS
            for suit in self.__SUITS
        ]
        random.shuffle(new_deck)
        return new_deck

    def __init__(self):
        self.__counter: int = 0
        self.__deck: List[str] = self.__shufle()

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.__counter < self.__DECK_SIZE:
            card = self.__deck[self.__counter]
            self.__counter += 1
            return card
        raise StopIteration

    def __len__(self) -> int:
        return self.__DECK_SIZE - self.__counter

    def reshufle(self) -> None:
        self.__deck[self.__counter :] = self.__shufle(
            self.__deck[self.__counter :]
        )

    def new_dist(self) -> None:
        print("_" * 80)
        self.__counter = 0
        self.reshufle()


def task5() -> None:
    deck = CardDeck()

    print(len(deck))
    for card in deck:
        print(card)

    deck.new_dist()
    for i in range(15):
        print(next(deck))
    print(len(deck))

    deck.new_dist()
    print(len(deck))
    for card in deck:
        print(card)
        deck.reshufle()


if __name__ == "__main__":
    task5()
