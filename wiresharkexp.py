import dpkt
import socket
def printPcap(pcap):
    try:
        eth=dpkt.ethernet.Ethernet(buf)
        ip=eth.data

        src=socket.inet_ntoa(ipsrc)

        dst= socket.inet_ntoa(ip.dst)
        print('Source : '+ src + 'Destination : '+ dst)
    
    except:
        pass

def main():
    f=open(r'C:/Users/acer pc/Desktop/ipaddrscapture.pcap', 'rb')
    pcap=dpkt.pcap.Reader(f)

    printPcap(pcap)
    
if __name__=='__main__':
   main()