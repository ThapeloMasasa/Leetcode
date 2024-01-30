# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climbingStairs(stairs):
    memo = {}
    def rec_steps(steps, memo):
        if steps <= 0 or steps == 1:
            return 1
        if steps in memo:
            return memo[steps]
        ways = rec_steps(steps - 1, memo) + rec_steps(steps - 2, memo)
        memo[steps] = ways
        return ways
    return rec_steps(stairs - 1, memo) 