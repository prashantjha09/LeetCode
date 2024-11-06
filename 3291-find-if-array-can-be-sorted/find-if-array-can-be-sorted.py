class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        lst = nums
        def get_bits(input_list):
            set_bits_list = []
            for number in input_list:
                set_bits = bin(number).count("1")
                set_bits_list.append(set_bits)
            return set_bits_list

        number = get_bits(lst)  
        initial_position_dict = {lst[element]: element for element in range(len(lst))}
        sorted_position_dict = {sorted(lst)[element]: element for element in range(len(sorted(lst)))}
        for i in sorted_position_dict:
            current_position = sorted_position_dict[i]
            initial_position = initial_position_dict[i]
            if current_position > initial_position:
                current_position, initial_position = initial_position, current_position
            s1 = max(number[current_position:initial_position+1])
            s2 = min(number[current_position:initial_position+1])
            if s1 != s2:
                return False
        return True
                