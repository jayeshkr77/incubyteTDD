import re

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if not numbers:
            return 0

        # Default delimiter
        delimiter = ','

        # Delimiter passed with the string
        if numbers.startswith("//"):
            parts = numbers.split('\n', 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
        
        # Mixed delimiters
        if delimiter != ',' and ',' in numbers:
            raise ValueError("invalid input, mixed delimiters not allowed")
        
        numbers = re.split(f"[{delimiter}\n]", numbers)
        
        num_list = [int(num) for num in numbers if num]
        
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")
        
        return sum(num_list)