class Solution:
    def calculate(self, s: str) -> int:
        
        total, curr, sign = 0, 0, 1
        stack = []

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)

            elif char == '+':
                total += sign * curr
                curr, sign = 0, 1

            elif char == '-':
                total += sign * curr
                curr, sign = 0, -1
                sign = -1

            elif char == '(':
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1

            elif char == ')':
                total += sign * curr
                curr = 0                
                prev_sign = stack.pop()
                prev_total = stack.pop()
                
                total = prev_total + (prev_sign * total)

        return total + (sign * curr)
