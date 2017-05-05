import masscan
from re import findall
def Gets(ip):
    mc = masscan.PortScanner()
    try:
        data = str(mc.scan(ip,ports = '22',arguments='--open -n'))
        xuly = list(set(findall(r'[0-9]+(?:\.[0-9]+){3}',data)))
        return xuly
    except:
        pass
if __name__ == '__main__':
     w = open('ip.txt', 'w+')
     source = open('VN.txt','r').read()
     ls = source.split()
     for i in ls:
          result = Gets(i)
          if (result != None) :
                for j in result:
                        w.write(j + '\n')
     w.close()
     print 'Success!'