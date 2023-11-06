"""
Puzzle
https://github.com/AnnaStasyshynn/stasyshyn-anna-lab8-task2.git
"""
def validate_board(board: list) -> bool:
    """
    >>> board = [\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
]
    >>> validate_board(board)
    False
    """
    pass

def get_sections(brd: list) -> list:
    """
    Get colored sections from board
    >>> board = [\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
]
    >>> get_sections(board)
    [['*', '*', '*', '*', ' ', ' ', '3', ' ', ' ', ' ', '2', ' ', ' ', '*', '*', '*', '*'], \
['*', '*', '*', ' ', ' ', '6', ' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
['*', '*', ' ', '4', ' ', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
['*', '1', ' ', ' ', ' ', ' ', '8', '3', ' ', ' ', '*'], \
[' ', ' ', '3', '1', ' ', '9', ' ', '5', ' '], ['*', '*', '*', '*', '*', '*', '*'], \
['*', '*', '*', '*', '*'], ['*', '*', '*'], ['*']]
    """
    brd = board_to_list(brd)
    sections = [[] for i in range(9)]
    counter = 8
    for i in range(9):
        for j in range(9):
            if j > counter:
                sections[counter].append(brd[i][j])
            else:
                sections[j].append(brd[i][j])
        counter -= 1
    return sections
