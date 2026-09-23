class Solution:
    def isValid(self, s: str) -> bool:

        stack = []  # Use a list as our stack

        for i in s:

            # 1. Opening bracket → put it onto the stack
            if i == '(' or i == '{' or i == '[':
                stack.append(i)

            # 2. Closing bracket
            elif i == ')' or i == '}' or i == ']':

                if not stack:
                    return False

                # Check whether the top of the stack matches
                # the closing bracket
                if i == ')' and stack[-1] == '(':
                    stack.pop()

                elif i == '}' and stack[-1] == '{':
                    stack.pop()

                elif i == ']' and stack[-1] == '[':
                    stack.pop()

                else:
                    # Closing bracket doesn't match the top
                    return False

        # We only decide whether the whole string is valid AFTER
        # processing every character.
        if not stack:
            return True
        else:
            return False