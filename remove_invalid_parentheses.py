class Solution(object):
    def removeInvalidParentheses(self, s):
        def is_valid(s):
            counter = 0
            value = { '(': 1, ')': -1 }
            for l in s:
                if l in ['(', ')']:
                    counter += value[l]
                    if counter < 0:
                        return False
            return counter == 0

        queue = set([s])
        valid = []

        while len(queue) and len(valid) == 0:
            next_queue = set()
            for i in range(len(queue)):
                item = queue.pop()
                if is_valid(item):
                    valid.append(item)
                else:
                    for i in range(len(item)):
                        next_queue.add((item[:i] + item[i+1:]))
            queue = next_queue

        return valid

print (Solution().removeInvalidParentheses('()())()'))
