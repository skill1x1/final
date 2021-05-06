"""
File: testqueue.py
Author: Ken Lambert
A tester program for queue implementations.
"""


from linkedqueue import LinkedQueue

def test(queueType):
    q = queueType()

    for i in range(4):
        q.add(i + 1)
    print("Adding 1 2 3 4:", q)
    q.remove(2)
    print("Removing 2:", q)
    q.remove(4)
    print("Removing 4:", q)
    q.remove(1)
    print("Removing 1:", q)
    q.remove(3)
    print("Removing 3:", q)
    print("Length:", len(q))
    print("Empty:", q.isEmpty())

test(LinkedQueue)
