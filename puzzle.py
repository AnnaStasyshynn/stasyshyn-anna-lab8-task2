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
