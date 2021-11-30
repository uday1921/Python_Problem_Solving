from  threading import Thread

class MYthread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    

    def run(self):
        for i in range(100000):
            msg = "%s is running" % \
                self.name
            print(msg)

def create_threads():
    for i in range(1000000):
        name = "Thread #%s" % (i + 1)
        my_thread = MYthread(name)
        my_thread.start()

create_threads()

