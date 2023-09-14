class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0  # Initialize the result variable to store the final integer value

        # Create a dictionary to store the mappings of Roman numerals to integers
        translations = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        n = len(s)  # Get the length of the input Roman numeral string

        # Iterate through each character in the input string
        for i in range(n):
            # Check if the current character is smaller than the next character
            if i + 1 < n and translations[s[i]] < translations[s[i + 1]]:
                res -= translations[s[i]]  # Subtract the current value from the result
            else:
                res += translations[s[i]]  # Add the current value to the result

        return res  # Return the final integer value
