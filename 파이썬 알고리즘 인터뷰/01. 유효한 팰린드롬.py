"""
01. 유효한 팰린드롬
"""
import collections
from typing import Deque


# 제출 답안
def isPalindrome(input_value: str) -> bool:
    input_value_length = len(input_value)

    first_compare_list = []
    second_compare_list = []

    for i in range(input_value_length):
        temp_char = input_value[i].lower()
        if temp_char.isalnum():
            first_compare_list.append(temp_char)

        temp_position = input_value_length - 1 - i

        temp_char_2 = input_value[temp_position].lower()
        if temp_char_2.isalnum():
            second_compare_list.append(temp_char_2)

    first_string = "".join(first_compare_list)
    second_string = "".join(second_compare_list)

    if first_string == second_string:
        return True
    else:
        return False


# 리스트로 변환
def isPalindromeWithList(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


# 데크 자료형을 이용한 최적화
def isPalindromeWithDeque(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


if __name__ == "__main__":
    s: str = "abba"

    print("# 내가 제출한 답안")
    if isPalindrome(s):
        print("true")
    else:
        print("false")

    print("# 리스트로 변환")
    if isPalindromeWithList(s):
        print("true")
    else:
        print("false")

    print("# 데크 자료형을 이용한 최적화")
    if isPalindromeWithDeque(s):
        print("true")
    else:
        print("false")
