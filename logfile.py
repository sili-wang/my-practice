class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []
        # Split the logs into letter logs and digit logs
        for log in logs:
            if log.split(" ")[1].isalpha():
                letter_log.append(log)
            else:
                digit_log.append(log)

        # Sort the letter logs lexicographically based on the content and then the identifiers

        letter_log.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))
        return letter_log + digit_log