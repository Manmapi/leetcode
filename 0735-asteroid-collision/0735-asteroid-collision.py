class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack or stack[-1] * ast > 0 or stack[-1] < 0:
                stack.append(ast)
            else:
                eleminated = False
                while stack and stack[-1] * ast < 0 and stack[-1] > 0:
                    if abs(stack[-1]) < abs(ast):
                        stack.pop()
                    elif abs(stack[-1]) == abs(ast):
                        eleminated = True
                        stack.pop()
                        break
                    else:
                        eleminated = True
                        break
                if not eleminated:
                    stack.append(ast)
        return stack