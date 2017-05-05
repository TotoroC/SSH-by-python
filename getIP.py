import nmap
from re import findall
import time


def Gets(ip):
    nm = nmap.PortScanner()
    data = str(nm.scan(ip,'22','--open -n'))
    xuly = list(set(findall(r'[0-9]+(?:\.[0-9]+){3}',data)))
    return xuly
if __name__ == '__main__':
     w = open('ip.txt', 'w+')
     source = open('VN.txt','r').read()
     srtime = time.time()
     ls = source.split()
     for i in ls:
          result = Gets(i)
          for j in result:
                   w.write(j + '\n')
     endtime = time.time()
     w.close()
     print 'total run-time: %f ms' % ((endtime - srtime) * 1000)


