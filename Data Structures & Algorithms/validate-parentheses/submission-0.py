class Solution:

    # defines a function that takes a string s and returns a boolean (True/False)
    def isValid(self, s: str) -> bool:

        # creates an empty list that we'll use as a stack
        # stores opening brackets that haven't been matched yet
        stack = []

        # creates a dictionary mapping each closing bracket (key) to its corresponding
        # opening bracket (value)
        pairs = {
            ")": "(",  # closing ")" matches opening "("
            "]": "[",  # closing "]" matches opening "["
            "}": "{"   # closing "}" matches opening "{"
        }

        # loops through every character in the input string s
        for char in s:

            # checks whether the current character is an opening bracket
            if char in "([{":

                # adds the opening bracket to the end (top) of the stack
                stack.append(char)

            # runs when the current character is a closing bracket
            else:

                # checks whether the stack is empty (no opening brackets available)
                if not stack:

                    # returns False because a closing bracket has no opening match
                    return False

                # checks whether the most recent opening bracket (stack[-1]) is DIFFERENT
                # from the expected opening bracket (pairs[char])
                if stack[-1] != pairs[char]:

                    # returns False because the brackets don't match
                    return False

                # removes most recent opening bracket bc it matched the current closing bracket
                stack.pop()

        # checks whether the stack is empty after processing all characters
        # an empty stack means every opening bracket was matched
        # a nonempty stack means some opening brackets were never closed
        return len(stack) == 0