import serial  # 导入模块
import binascii
import threading


class UartInfo(object):
    def __init__(self, fd, fdstate, otafile):
        self.fd = fd
        self.fdstate = fdstate
        self.otafile = otafile


uart =  UartInfo(-1, False, r"F:\Python_Workspace\python_study\uart\LeBleGetway_V1.0.4.bin")


def hexShow(argv):        #十六进制显示 方法1
    try:
        result = ''
        hLen = len(argv)
        for i in range(hLen):
         hvol = argv[i]
         hhex = '%02x'%hvol
         result += hhex+' '
         print('hexShow:', result)
    except:
        pass

def crc_sum(puchMsg, usDataLen):
    sum = 0;
    i = 0;
    while(i < usDataLen):
        sum += puchMsg[i]
        i += 1
    return sum & 0x00FF

# 打开串口
# 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
def DOpenPort(portx, bps, timeout):
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timeout)
        # 判断是否打开成功
        if(False == ser.is_open):
           ser = -1
    except Exception as e:
        print("---异常---：", e)
    return ser


# 关闭串口
def DColsePort(ser):
    uart.fdstate = False
    ser.close()


# 写数据
def DWritePort(ser, text):
    result = ser.write(bytes.fromhex(text))  # 写数据
    return result


# 读数代码本体实现
def Led2_4_ReadData(ser):
    # 循环接收数据，此为死循环，可用线程实现
    while(True == uart.fdstate):
        if ser.in_waiting:
            try:  # 如果读取的不是十六进制数据--
                data = str(binascii.b2a_hex(ser.read(ser.in_waiting)))[2:-1]  # 十六进制显示方法2
                print(data)
            except:  # --则将其作为字符串读取
                str = ser.read(ser.in_waiting)
                hexShow(str)


def Led2_4_GetOtaVersion():
    with open(uart.otafile, 'rb') as otafd:
        otafd.seek(0, 0)
        otafd.seek(0, 2)

        if(otafd.tell() > 32):
            otafd.seek(0, 0)
            version = otafd.read(32)
            print(version)
            otafd.close()
            return True
        else:
            otafd.close()
            return False


def Led2_4_StartOta():
    with open(uart.otafile, 'rb') as otafd:
        otafd.seek(0, 0)
        otafd.seek(0, 2)
        filelength = otafd.tell()

        writebuffer = "55 aa 00 21 00 04" +  str(hex(filelength))
        print(writebuffer)
        count = DWritePort(uart.fd, writebuffer)
        print("写入字节数：", count)


def Led2_4_UpgradeProcess(ser):
    # 循环接收数据，此为死循环，可用线程实现
    if(True == uart.fdstate):
        if (True == Led2_4_GetOtaVersion()):
            print("GetOtaVersion OK")
        if (True == Led2_4_StartOta()):
            print("StartOta OK")

if __name__ == "__main__":
    uart.fd = DOpenPort("COM4", 115200, None)
    print("uart.fd", uart.fd)
    if(uart.fd != -1):  # 判断串口是否成功打开
        uart.fdstate = True
        threading.Thread(target=Led2_4_UpgradeProcess, args=(uart.fd,)).start()
        threading.Thread(target=Led2_4_ReadData, args=(uart.fd,)).start()

    #DColsePort(ser)  # 关闭串口
