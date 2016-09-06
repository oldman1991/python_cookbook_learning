# coding=utf-8

#优先级队列
import heapq
import itertools

pq = []  # list of entries arranged in a heap
entry_finder = {} # mapping of tasks to entries
REMOVE = u'<removed-task>' # placeholder for a removed task
counter = itertools.count() # unique sequence count

def add_task(task,priority=0):
    "Add a new task or update the priority of an existing task"
    if task in entry_finder:
        remove_task(task)
    count=next(counter)
    entry=[priority,count,task]
    entry_finder[task] = entry
    heapq.heappush(pq,entry)



def remove_task(task):
    "Mark an existing task as REMOVED.  Raise KeyError if not found. "
    entry = entry_finder.pop(task)
    entry[-1]=REMOVE
    print(id(entry))
    print(id(pq[0]))


def pop_task():
    "Remove and return the lowest priority task. Raise KeyError if empty."
    while pq:
        priority,count,task=heapq.heappop(pq)
        if task is not REMOVE:
            del entry_finder[task]
            return task


# add_task(1222)
# add_task(1222)
# add_task(1)
if __name__=="__main__":
    list_res=[1,2,3,5,7,9]
    a=heapq.heappop(list_res)
    print(a)
