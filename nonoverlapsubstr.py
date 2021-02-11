class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        def get_substring_right(s, left_bound, right_bound, bound):
            right_most = right_bound

            i = left_bound
            while i <= right_most:
                letter = s[i]
                left, right = bound[letter]

                if left < left_bound:
                    return -1

                right_most = max(right_most, right)

                i += 1

            return right_most

        bound = {}
        for i in range(len(s)):
            letter = s[i]
            if letter not in bound:
                bound[letter] = [i, i]
            bound[letter][1] = i

        substrings = []

        last_recorded_right = -1
        for i in range(len(s)):
            letter = s[i]
            left, right = bound[letter]

            if i == left:
                substring_right = get_substring_right(s, left, right, bound)

                # self contained substring
                if substring_right != -1:
                    if last_recorded_right < left:
                        substrings.append("")

                    last_recorded_right = substring_right
                    substrings[-1] = s[i:last_recorded_right + 1]

        return substrings