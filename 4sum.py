nums.sort()
answer = []
for i in range(len(nums) - 3):
    if i != 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, len(nums) - 2):
        if j != i + 1 and nums[j] == nums[j - 1]:
            continue

        find = target - nums[i] - nums[j]

        lower = j + 1
        higher = len(nums) - 1

        while lower < higher:
            if nums[lower] + nums[higher] < find:
                lower += 1

            elif nums[lower] + nums[higher] > find:
                higher -= 1

            else:
                answer.append([nums[lower], nums[higher], nums[i], nums[j]])
                while lower < higher and nums[lower] == nums[lower + 1]:
                    lower += 1

                while lower < higher and nums[higher] == nums[higher - 1]:
                    higher -= 1
                lower += 1
                higher -= 1
return answer