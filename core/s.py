import serial
import serial.tools.list_ports
import time
import threading

def getPortList():
    for i in list(serial.tools.list_ports.comports()):
        i.description
    return list(serial.tools.list_ports.comports())

class myserial():
    def __init__(self, port="", bund=0):
        self.read_flag = False
        self.port = port
        self.bund = bund

    def setSer(self, port:str, bund:int):
        self.port = port
        self.bund = bund

    def open(self, fun, timeout = 1000):
        try:
            self.ser = serial.Serial(self.port, self.bund, timeout=timeout)
            if self.ser.is_open:
                self.read_flag = True
                rt = threading.Thread(target=self.loopRead, args=(fun,))
                rt.setDaemon(True)
                rt.start()
                
                return 0, "打开串口%s成功,波特率%d\n" % (self.port, self.bund)
        except Exception as e:
            self.read_flag = False
            return 1, "打开串口%s失败\n%s\n" % (self.port, str(e))

    def write(self, text):
        result = self.ser.write(text.encode('utf-8'))
        return result
        
    def loopRead(self, fun):
        while self.read_flag:
            try:
                if self.ser.in_waiting:
                    txt = self.ser.read(self.ser.in_waiting).decode("utf-8")
                    fun(txt)
            except:
                self.loopRead = False

    def stop(self):
        self.read_flag = False
        self.ser.close()