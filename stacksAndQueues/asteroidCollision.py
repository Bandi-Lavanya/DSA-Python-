def asteroidCollision_brute(asteroids):
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(asteroids) - 1:
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                # collision
                if abs(asteroids[i]) > abs(asteroids[i+1]):
                    asteroids.pop(i+1)  # right one explodes
                elif abs(asteroids[i]) < abs(asteroids[i+1]):
                    asteroids.pop(i)    # left one explodes
                else:
                    asteroids.pop(i+1)
                    asteroids.pop(i)
                changed = True
                break  # restart after modification
            else:
                i += 1
    return asteroids

print(asteroidCollision_brute([4,7,1,1,2,-3,-7,17,15,-16]))  # [4,17]


def asteroidCollision_better(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 < stack[-1]:
            if stack[-1] < -a:  # right smaller, pop
                stack.pop()
                continue
            elif stack[-1] == -a:  # equal, both explode
                stack.pop()
            break
        else:
            stack.append(a)
    return stack

print(asteroidCollision_better([4,7,1,1,2,-3,-7,17,15,-18,-19]))  # [4,17]

def asteroidCollision_optimal(asteroids):
    stack = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:  # fix is here
            if stack[-1] < -a:   # top asteroid is smaller -> destroyed
                stack.pop()
                continue
            elif stack[-1] == -a:  # both equal -> both destroyed
                stack.pop()
            alive = False
        if alive:
            stack.append(a)
    return stack


# Example
print(asteroidCollision_optimal([4,7,1,1,2,-3,-7,17,15,-16]))  # [4, 17]
