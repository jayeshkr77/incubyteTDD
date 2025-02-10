import re

class StringCalculator:

    @staticmethod
    def getDelimeter(numbers):
        delimiter = ','

        # Delimiter passed with the string
        if numbers.startswith("//"):
            parts = numbers.split('\n', 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
        
        # Mixed delimiters
        if delimiter != ',' and ',' in numbers:
            raise ValueError("invalid input, mixed delimiters not allowed")
        
        return delimiter, numbers

    @staticmethod
    def convertToNumArray(numbers, delimiter):
        numbers = re.split(f"[{delimiter}\n]", numbers)
        num_list = [int(num) for num in numbers if num]
        return num_list

    def cleanup(fn):
        def dec(numbers):
            # Default delimiter
            delimiter, numbers = StringCalculator.getDelimeter(numbers)           
            return fn(StringCalculator.convertToNumArray(numbers, delimiter))
        return dec


    @staticmethod
    @cleanup
    def add(numbers: int) -> int:
        if not numbers:
            return 0
        negatives = [num for num in numbers if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")
        
        return sum(numbers)