import sys
import threading
import time


class Move(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


class Fork(object):

    def __init__(self, number):
        self.number = number
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):

        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("p[%s] took c[%s]\n" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("p[%s] dropped c[%s]\n" % (user, self.number))
            self.lock.notifyAll()


class Philosopher(threading.Thread):

    def __init__(self, number, left, right, waiter):
        threading.Thread.__init__(self)
        self.number = number  # philosopher number
        self.left = left
        self.right = right
        self.waiter = waiter

    def run(self):
        for i in range(5):
            self.waiter.down()  # start service by waiter
            time.sleep(0.1)  # think
            self.left.take(self.number)  # pickup left fork
            time.sleep(0.1)  # (yield makes deadlock more likely)
            self.right.take(self.number)  # pickup right fork
            time.sleep(0.1)  # eat
            self.right.drop(self.number)  # drop right fork
            self.left.drop(self.number)  # drop left fork
            self.waiter.up()  # end service by waiter

        sys.stdout.write("p[%s] finished thinking and eating\n" % self.number)


def main():

    n = 5 # number of philosophers / forks
    waiter = Move(n - 1) # waiter for deadlock avoidance (n-1 available)
    c = [Fork(i) for i in range(n)] #forks
    p = [Philosopher(i, c[i], c[(i + 1) % n], waiter) for i in range(n)]  #philsophers

    for i in range(n):
        p[i].start()


main()