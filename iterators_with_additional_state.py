# coding=utf-8
from collections import deque


class linehistory():
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 0):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == "__main__":
    with open('somefile.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, line in lines.history:
                    print('{}:{}'.format(lineno, line), end='')
