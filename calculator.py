#This file is a modification of 2013 Kevin Tseng's holdem calculator
#here is a link to his work: https://github.com/ktseng/holdem_calc
#and here is his license:

'''
Copyright (c) 2013 Kevin Tseng

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import random
import time
import itertools

class CalculatingCard:
    def __init__(self, hand):
        self.hand = hand
        self.value = 0
        if hand[0] == 't':
            self.value = 10
        elif hand[0] == 'j':
            self.value = 11
        elif hand[0] == 'q':
            self.value = 12
        elif hand[0] == 'k':
            self.value = 13
        elif hand[0] == 'a':
            self.value = 14
        else:
            try:
                self.value = int(hand[0])
            except:
                print("error in CalculatingCard rank")
                dumb = input("]")

        self.suit = hand[1]
        self.suit_index = 0
        if self.suit == 's':
            self.suit_index = 0
        elif self.suit == 'c':
            self.suit_index = 1
        elif self.suit == 'h':
            self.suit_index = 2
        elif self.suit == 'd':
            self.suit_index = 3
        else:
            print("error in CalculatingCard suit")
            dumb = input("]")

    def __str__(self):
        return self.hand

    def __repr__(self):
        return self.hand

    def __eq__(self, other):
        if self is None:
            return other is None
        elif other is None:
            return False
        return self.value == other.value and self.suit == other.suit

def find_equx(card1, card2, board):
    card3 = None
    card4 = None

    hole_cards1 = (card1, card2)
    hole_cards2 = (card3, card4)
    hole_cards = (hole_cards1, hole_cards2)
    return run(hole_cards, board)

def find_equity(list_cards, board):
    hole_cards = []
    if len(list_cards) == 4: #2 gamblers 
        card1 = list_cards[0]
        card2 = list_cards[1]
        card3 = list_cards[2]
        card4 = list_cards[3]
        hole_cards1 = (card1, card2)
        hole_cards2 = (card3, card4)
        hole_cards = (hole_cards1, hole_cards2)
    elif len(list_cards) == 6: #3 gamblers 
        card1 = list_cards[0]
        card2 = list_cards[1]
        card3 = list_cards[2]
        card4 = list_cards[3]
        card5 = list_cards[4]
        card6 = list_cards[5]
        hole_cards1 = (card1, card2)
        hole_cards2 = (card3, card4)
        hole_cards3 = (card5, card6)
        hole_cards = (hole_cards1, hole_cards2, hole_cards3)
    elif len(list_cards) == 8: #4 gamblers 
        card1 = list_cards[0]
        card2 = list_cards[1]
        card3 = list_cards[2]
        card4 = list_cards[3]
        card5 = list_cards[4]
        card6 = list_cards[5]
        card7 = list_cards[6]
        card8 = list_cards[7]
        hole_cards1 = (card1, card2)
        hole_cards2 = (card3, card4)
        hole_cards3 = (card5, card6)
        hole_cards4 = (card7, card8)
        hole_cards = (hole_cards1, hole_cards2, hole_cards3, hole_cards4)
    elif len(list_cards) == 10: #5 gamblers 
        card1 = list_cards[0]
        card2 = list_cards[1]
        card3 = list_cards[2]
        card4 = list_cards[3]
        card5 = list_cards[4]
        card6 = list_cards[5]
        card7 = list_cards[6]
        card8 = list_cards[7]
        card9 = list_cards[8]
        card10 = list_cards[9]
        hole_cards1 = (card1, card2)
        hole_cards2 = (card3, card4)
        hole_cards3 = (card5, card6)
        hole_cards4 = (card7, card8)
        hole_cards5 = (card9, card10)
        hole_cards = (hole_cards1, hole_cards2, hole_cards3, hole_cards4, hole_cards5)
    elif len(list_cards) == 12: #6 gamblers 
        card1 = list_cards[0]
        card2 = list_cards[1]
        card3 = list_cards[2]
        card4 = list_cards[3]
        card5 = list_cards[4]
        card6 = list_cards[5]
        card7 = list_cards[6]
        card8 = list_cards[7]
        card9 = list_cards[8]
        card10 = list_cards[9]
        card11 = list_cards[10]
        card12 = list_cards[11]
        hole_cards1 = (card1, card2)
        hole_cards2 = (card3, card4)
        hole_cards3 = (card5, card6)
        hole_cards4 = (card7, card8)
        hole_cards5 = (card9, card10)
        hole_cards6 = (card11, card12)
        hole_cards = (hole_cards1, hole_cards2, hole_cards3, hole_cards4, hole_cards5, hole_cards6)
    else:
        print("unsupported number of gamblers in calculator.py")
        dumb = input("]")
    return run(hole_cards, board)

def run(hole_cards, board):
    deck = shuffle_deck(hole_cards, board)
    return list(run_simulation(hole_cards, board, deck))

def detect_straight_flush(suit_board):
    contiguous_length, fail_index = 1, len(suit_board) - 5
    for index, elem in enumerate(suit_board):
        current_val, next_val = elem, suit_board[index + 1]
        if next_val == current_val - 1:
            contiguous_length += 1
            if contiguous_length == 5:
                return True, current_val + 3
        else:
            if index >= fail_index:
                if (index == fail_index and next_val == 5 and
                        suit_board[0] == 14):
                    return True, 5
                break
            contiguous_length = 1
    return False,

def detect_highest_quad_kicker(board):
    for elem in board:
        if elem[1] < 4:
            return elem[0]

def detect_straight(board):
    contiguous_length, fail_index = 1, len(board) - 5
    for index, elem in enumerate(board):
        current_val, next_val = elem[0], board[index + 1][0]
        if next_val == current_val - 1:
            contiguous_length += 1
            if contiguous_length == 5:
                return True, current_val + 3
        else:
            if index >= fail_index:
                if (index == fail_index and next_val == 5 and
                        board[0][0] == 14):
                    return True, 5
                break
            contiguous_length = 1
    return False,

def detect_three_of_a_kind_kickers(board):
    kicker1 = -1
    for elem in board:
        if elem[1] != 3:
            if kicker1 == -1:
                kicker1 = elem[0]
            else:
                return kicker1, elem[0]

def detect_highest_kicker(board):
    for elem in board:
        if elem[1] == 1:
            return elem[0]

def detect_pair_kickers(board):
    kicker1, kicker2 = -1, -1
    for elem in board:
        if elem[1] != 2:
            if kicker1 == -1:
                kicker1 = elem[0]
            elif kicker2 == -1:
                kicker2 = elem[0]
            else:
                return kicker1, kicker2, elem[0]

def get_high_cards(board):
    return board[:5]

def preprocess(histogram):
    return [(14 - index, frequency) for index, frequency in
            enumerate(histogram) if frequency]

def detect_hand(hole_cards, given_board, suit_histogram,
                full_histogram, max_suit):
    if max_suit >= 3:
        flush_index = suit_histogram.index(max_suit)
        for hole_card in hole_cards:
            if hole_card.suit_index == flush_index:
                max_suit += 1
        if max_suit >= 5:
            flat_board = list(given_board)
            flat_board.extend(hole_cards)
            suit_board = generate_suit_board(flat_board, flush_index)
            result = detect_straight_flush(suit_board)
            if result[0]:
                return (8, result[1]) if result[1] != 14 else (9,)
            return 5, get_high_cards(suit_board)

    full_histogram = full_histogram[:]
    for hole_card in hole_cards:
        full_histogram[14 - hole_card.value] += 1
    board = preprocess(full_histogram)

    current_max, max_val, second_max, second_max_val = 0, 0, 0, 0
    for item in board:
        val, frequency = item[0], item[1]
        if frequency > current_max:
            second_max, second_max_val = current_max, max_val
            current_max, max_val = frequency, val
        elif frequency > second_max:
            second_max, second_max_val = frequency, val

    if current_max == 4:
        return 7, max_val, detect_highest_quad_kicker(board)
    if current_max == 3 and second_max >= 2:
        return 6, max_val, second_max_val
    if len(board) >= 5:
        result = detect_straight(board)
        if result[0]:
            return 4, result[1]
    if current_max == 3:
        return 3, max_val, detect_three_of_a_kind_kickers(board)
    if current_max == 2:
        if second_max == 2:
            return 2, max_val, second_max_val, detect_highest_kicker(
                board)
        else:
            return 1, max_val, detect_pair_kickers(board)
    return 0, get_high_cards(board)

def preprocess_board(board):
    suit_histogram, histogram = [0] * 4, [0] * 13
    for card in board:
        histogram[14 - card.value] += 1
        suit_histogram[card.suit_index] += 1
    return suit_histogram, histogram, max(suit_histogram)

def whowins(rand_boards, deck, hole_cards, board_length,
                dealt_board, winners):
    result_list = [None] * len(hole_cards)
    for remaining_board in rand_boards(deck, 1, board_length):
        if dealt_board:
            board = dealt_board[:]
            board.extend(remaining_board)
        else:
            board = remaining_board
        suit_histogram, histogram, max_suit = (
            preprocess_board(board))
        for index, hole_card in enumerate(hole_cards):
            result_list[index] = detect_hand(hole_card, board, suit_histogram,
                                             histogram, max_suit)
        winner_index = compare_hands(result_list)
        winners[winner_index] += 1

def find_winning_percentage(winner_list):
    float_iterations = float(sum(winner_list))
    percentages = []
    for num_wins in winner_list:
        winning_percentage = float(num_wins) / float_iterations
        percentages.append(winning_percentage)
    return list(percentages)

def compare_hands(result_list):
    best_hand = max(result_list)
    winning_player_index = result_list.index(best_hand) + 1
    if best_hand in result_list[winning_player_index:]:
        return 0
    return winning_player_index

def generate_suit_board(flat_board, flush_index):
    histogram = [card.value for card in flat_board
                 if card.suit_index == flush_index]
    histogram.sort(reverse=True)
    return histogram

def deal_cards(deck):
    return itertools.combinations(deck, 2)

def shuffle_cards(deck, iterations, board_length):
    random.seed(time.time())
    for _ in range(iterations):
        yield random.sample(deck, 5 - board_length)


def run_simulation(hole_cards, t_board, deck):
    gamblers = len(hole_cards)
    winners = [0] * (gamblers + 1)
    board_len = 0 if t_board is None else len(t_board)
    generate_boards = shuffle_cards
    if (None, None) in hole_cards:
        hole_cards_list = list(hole_cards)
        unknown_index = hole_cards.index((None, None))
        for filler_hole_cards in deal_cards(deck):
            hole_cards_list[unknown_index] = filler_hole_cards
            deck_list = list(deck)
            deck_list.remove(filler_hole_cards[0])
            deck_list.remove(filler_hole_cards[1])
            whowins(generate_boards, tuple(deck_list),
                                         tuple(hole_cards_list),
                                         board_len, t_board, winners)
    else:
        whowins(generate_boards, deck, hole_cards, board_len, t_board, winners)
    return list(find_winning_percentage(winners))

def shuffle_deck(hole_cards, board):
    deck = []
    suits = ("s", "c", "h", "d")
    ranks = "akqjt98765432"
    for suit in suits:
        for rank in ranks:
            deck.append(CalculatingCard(rank + suit))
    
    '''
    burned_cards = []
    for hole_card in hole_cards:
        for card in hole_card:
            if card is not None:
                burned_cards.append(card)
    if board and len(board) > 0:
        burned_cards.extend(board)


    for dealt_card in burned_cards:
        try:
            deck.remove(dealt_card)
        except:
            print("dealt_card: " + str(dealt_card))
            print("deck: ")
            print(deck)
            dumb = input("]")
     '''   

    return tuple(deck)
