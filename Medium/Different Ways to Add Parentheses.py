class Solution:

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        def evaluate(num1, num2, expr):
            if expr == '+':
                return num1 + num2
            elif expr == '-':
                return num1 - num2
            elif expr == '*':
                return num1 * num2

        memo = dict()

        def dfs(expression):

            if expression in memo:
                return memo[expression]

            if expression.isnumeric():
                return [int(expression)]

            results = list()

            for ind, char in enumerate(expression):
                if char.isnumeric():
                    continue

                expr = char
                left_results = dfs(expression[:ind])
                right_results = dfs(expression[ind + 1:])

                for left in left_results:
                    for right in right_results:
                        results.append(evaluate(left, right, expr))

            memo[expression] = results
            return results

        return dfs(input)


if __name__ == '__main__':
    expression = "2*3-4"
    print(Solution().diffWaysToCompute(expression))
