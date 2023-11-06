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
def columns(board: list) -> list[list]:
    """
    Return a list of columns.
    >>> columns(board)
    [['*', '*', '*', '*', ' ', ' ', '3', ' ', ' '], ['*', '*', '*', ' ', ' ', '6', ' ', ' ', ' '], \
['*', '*', ' ', '4', ' ', ' ', ' ', '8', '2'], ['*', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' '], \
[' ', ' ', '3', '1', ' ', '8', '1', ' ', ' '], ['*', '*', '*', '*', '9', '3', ' ', '2', '*'], \
['*', '*', '*', '*', ' ', ' ', ' ', '*', '*'], ['*', '*', '*', '*', '5', ' ', '*', '*', '*'], \
['*', '*', '*', '*', ' ', '*', '*', '*', '*']]
    """
    cols = []
    for i in range(9):
        cols.append([n[i] for n in board])
    return cols
def board_to_list(board: list) -> list[list]:
    """
    Turn board into a list of lists containing
    each slot of of the board.
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
    >>> board_to_list(board)
    [['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], \
['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
[' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
[' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
[' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
[' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]
    """
    new_board = [list(l) for l in board]
    return new_board

 def check_section(section: list) -> bool | None:
    """
    Check if a section:
    - contains numbers from 1 to 9
    - contains unique numbers
    >>> check_section(['1', '2', '3'])
    True
    >>> check_section(['1', '12'])
    False
    >>> check_section(['1', '1'])
    False
    """
    nums = [int(n) for n in section if n.isdigit()]
    nums_set = set(nums)
    if len(nums) != len(nums_set):
        return False
    for i in nums:
        if i > 9:
            return False
    return True
def get_sections():
    pass
