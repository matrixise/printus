#!/usr/bin/env python

from rq import Queue, Worker, Connection

if __name__ == '__main__':
    with Connection():
        q = Queue()
        Worker(q).work()
