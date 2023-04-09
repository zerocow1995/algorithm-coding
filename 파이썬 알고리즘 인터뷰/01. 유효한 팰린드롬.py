"""
01. 유효한 팰린드롬
"""

# 제출 답안
if __name__ == "__main__":
    input_value = input("> ")
    value_length = len(input_value)

    first_compare_list = []
    second_compare_list = []

    for i in range(value_length):
        temp_char = input_value[i].lower()
        if temp_char.isalnum():
            first_compare_list.append(temp_char)

        temp_position = value_length - 1 - i

        temp_char_2 = input_value[temp_position].lower()
        if temp_char_2.isalnum():
            second_compare_list.append(temp_char_2)

    first_string = "".join(first_compare_list)
    second_string = "".join(second_compare_list)

    if first_string == second_string:
        print("true")
    else:
        print("false")

# 리스트로 변환
