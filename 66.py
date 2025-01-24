class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))  
        num = num + 1  
        num_str = str(num)  
        digits_incremented = [int(digit) for digit in num_str]  
        return(digits_incremented) 