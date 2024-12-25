class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                eleminated = False
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(ast):
                        eleminated = True
                        break
                    elif stack[-1] == abs(ast):
                        eleminated = True
                        stack.pop()
                        break
                    else:
                        stack.pop()
                if not eleminated:
                    stack.append(ast)
        return stack