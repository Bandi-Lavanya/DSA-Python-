def combination_sum2(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, target, path):
        if target == 0: #means we found a valid combination
            result.append(path[:]) #[:] ensures a copy is stored, not a reference
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]: # i > start ensures that only consecutive duplicates are skipped
                continue  # Skip duplicates
            if candidates[i] > target:
                break  # Stop further exploration
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()  # Undo last selection, necessary to explore other combinations in further iterations.


    backtrack(0, target, [])
    return result



numbers = [10, 1, 2, 7, 6, 1, 5]
result = combination_sum2(numbers, 8)
print(result)
