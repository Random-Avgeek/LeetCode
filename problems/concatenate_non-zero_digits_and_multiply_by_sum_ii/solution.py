class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)
        powers_of_10 = [1] * (n + 1)
        for i in range(1, n + 1):
            powers_of_10[i] = (powers_of_10[i - 1] * 10) % MOD
        prefix_sum_of_digits = [0] * (n + 1)
        prefix_count_non_zeros = [0] * (n + 1)
        prefix_concatenated_value = [0] * (n + 1)
        for i in range(n):
            current_digit = int(s[i])
            prefix_sum_of_digits[i + 1] = prefix_sum_of_digits[i] + current_digit
            
            if current_digit > 0:
                prefix_count_non_zeros[i + 1] = prefix_count_non_zeros[i] + 1
                prefix_concatenated_value[i + 1] = (prefix_concatenated_value[i] * 10 + current_digit) % MOD
            else:
                prefix_count_non_zeros[i + 1] = prefix_count_non_zeros[i]
                prefix_concatenated_value[i + 1] = prefix_concatenated_value[i]
        ans = []
        for left_index, right_index in queries:
            sum_in_range = prefix_sum_of_digits[right_index + 1] - prefix_sum_of_digits[left_index]
            non_zeros_in_range = prefix_count_non_zeros[right_index + 1] - prefix_count_non_zeros[left_index]
            left_part_to_remove = prefix_concatenated_value[left_index] * powers_of_10[non_zeros_in_range]
            concatenated_val_in_range = (prefix_concatenated_value[right_index + 1] - left_part_to_remove) % MOD
            final_result = (concatenated_val_in_range * sum_in_range) % MOD
            ans.append(final_result)
            
        return ans