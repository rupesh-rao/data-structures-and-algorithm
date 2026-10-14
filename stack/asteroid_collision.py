class Solution:
    def asteroidCollision(self, asteroids):
        ans = []
        for asteroid in asteroids:
            # add to stack if positive element
            if asteroid >= 0:
                ans.append(asteroid)
            else:
                # pop stack till positive top element is less than negative element
                # if stack top is negative then don't pop
                while ans and 0 < ans[-1] < -asteroid:
                    ans.pop()
                # remove top is equal to negative
                if ans and ans[-1] == -asteroid:
                    ans.pop()
                # add negative element to stack, if stack is empty
                # or top of stack is negative element
                elif not ans or ans[-1] < 0:
                    ans.append(asteroid)
        # return the stack
        return ans
