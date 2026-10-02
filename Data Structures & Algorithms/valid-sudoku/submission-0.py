class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def create_digit_dict():

            digit_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0,
                            7:0,  8:0, 9:0}
            return digit_dict

        for i in range(9):
            digit_dict_line = create_digit_dict()
            digit_dict_column = create_digit_dict()
            for j in range(9):
                if board[i][j] != ".":
                    digit_dict_line[int(board[i][j])] += 1
                    if digit_dict_line[int(board[i][j])] == 2:
                        return False
                if board[j][i] != ".":
                    digit_dict_column[int(board[j][i])] += 1
                    if digit_dict_column[int(board[j][i])] == 2:
                        return False


        def is_square_valid(board, L_1, L_2):
            digit_dict_square = create_digit_dict()
            for i in L_1:
                for j in L_2:
                    if board[i][j] != ".":
                        digit_dict_square[int(board[i][j])] += 1
                        if digit_dict_square[int(board[i][j])] > 1:
                            return False
            return True

        a = [0, 1, 2]
        b = [3, 4 ,5]
        c = [6, 7, 8]
        L = [a, b, c]
    
        for i in range(3):
            for j in range(3):
                if not is_square_valid(board, L[i], L[j]):
                    print("L[i]", L[i], "L[j]: ", L[j])
                    return False
    
        return True