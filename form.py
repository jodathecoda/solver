#copyright (c) 2019
#jodathecoda@yahoo.com
 
import calculator

def format_card_for_calculating(card):
	string_card = card[0] + card[1]
	formatted_card = calculator.CalculatingCard(string_card)
	return formatted_card

def format_board_for_calculating(board):
	board_list = []
	if len(board) == 6:
		c10 = board[0]
		c11 = board[1]
		c1 = c10 + c11
		fc1 = calculator.CalculatingCard(c1)
		board_list.append(fc1)

		c20 = board[2]
		c21 = board[3]
		c2 = c20 + c21
		fc2 = calculator.CalculatingCard(c2)
		board_list.append(fc2)

		c30 = board[4]
		c31 = board[5]
		c3 = c30 + c31
		fc3 = calculator.CalculatingCard(c3)
		board_list.append(fc3)

	elif len(board) == 8:
		c10 = board[0]
		c11 = board[1]
		c1 = c10 + c11
		fc1 = calculator.CalculatingCard(c1)
		board_list.append(fc1)

		c20 = board[2]
		c21 = board[3]
		c2 = c20 + c21
		fc2 = calculator.CalculatingCard(c2)
		board_list.append(fc2)

		c30 = board[4]
		c31 = board[5]
		c3 = c30 + c31
		fc3 = calculator.CalculatingCard(c3)
		board_list.append(fc3)

		c40 = board[6]
		c41 = board[7]
		c4 = c40 + c41
		fc4 = calculator.CalculatingCard(c4)
		board_list.append(fc4)

	elif len(board) == 10:
		c10 = board[0]
		c11 = board[1]
		c1 = c10 + c11
		fc1 = calculator.CalculatingCard(c1)
		board_list.append(fc1)

		c20 = board[2]
		c21 = board[3]
		c2 = c20 + c21
		fc2 = calculator.CalculatingCard(c2)
		board_list.append(fc2)

		c30 = board[4]
		c31 = board[5]
		c3 = c30 + c31
		fc3 = calculator.CalculatingCard(c3)
		board_list.append(fc3)

		c40 = board[6]
		c41 = board[7]
		c4 = c40 + c41
		fc4 = calculator.CalculatingCard(c4)
		board_list.append(fc4)

		c50 = board[8]
		c51 = board[9]
		c5 = c50 + c51
		fc5 = calculator.CalculatingCard(c5)
		board_list.append(fc5)
	else:
		print("unknown board length")
		dumb = input("]")

	return board_list