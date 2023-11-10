import unittest
import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

x_turn = [
    [EMPTY, EMPTY, O],
    [EMPTY, X, EMPTY],
    [X, EMPTY, O]
]

o_turn = [
    [EMPTY, EMPTY, O],
    [EMPTY, X, X],
    [X, EMPTY, O]
]

post_o_turn = [
    [EMPTY, EMPTY, O],
    [O, X, X],
    [X, EMPTY, O]
]

x_won = [
    [O, X, O],
    [EMPTY, X, EMPTY],
    [X, X, O]
]

o_won = [
    [X, EMPTY, O],
    [EMPTY, X, O],
    [X, EMPTY, O]
]

draw = [
    [X, O, O],
    [O, X, X],
    [X, X, O]
]

def print_board(board):
    row_string = ""

    for row in board:
        row_string += '\n'
        for col in row:
            if col == None:
                col = " "
            row_string += f'{col} '

    print(row_string)

class TestTictactoe(unittest.TestCase):
    def test_x_turn(self):
        turn = ttt.player(x_turn)
        self.assertEqual(turn, X)

    def test_o_turn(self):
        turn = ttt.player(o_turn)
        self.assertEqual(turn, O)

    def test_actions_set(self):
        actions = ttt.actions(x_turn)
        correct_set = (
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 2),
            (2, 1),
        )
        self.assertEqual(sorted(actions), sorted(correct_set))

    def test_draw_actions(self):
        actions = ttt.actions(draw)
        self.assertEqual(actions, set())

    def test_result_after_x_turn(self):
        new_board = ttt.result(x_turn, (1, 2))
        self.assertEqual(new_board, o_turn)

    def test_result_after_o_turn(self):
        new_board = ttt.result(o_turn, (1, 0))
        self.assertEqual(new_board, post_o_turn)

    def test_x_won(self):
        winner = ttt.winner(x_won)
        self.assertEqual(winner, X)

    def test_o_won(self):
        winner = ttt.winner(o_won)
        self.assertEqual(winner, O)
    
    def test_no_winner(self):
        self.assertEqual(ttt.winner(draw), None)
        self.assertEqual(ttt.winner(x_turn), None)

    def test_state_ended(self):
        self.assertTrue(ttt.terminal(x_won))
        self.assertTrue(ttt.terminal(o_won))
        self.assertTrue(ttt.terminal(draw))
        self.assertFalse(ttt.terminal(x_turn))
        self.assertFalse(ttt.terminal(o_turn))

    def test_outcome(self):
        self.assertEqual(ttt.utility(x_won), 1)
        self.assertEqual(ttt.utility(o_won), -1)
        self.assertEqual(ttt.utility(draw), 0)

if __name__ == '__main__':
    unittest.main()
    