import socket
import dpkt

s= socket.socket(socket.AF_INET, socket.SOCK_RAW,dpkt.ip.IP_PROTO_ICMP)

while True:
    
    packet= s.recvfrom(1024)


    
    print(packet)
    
    #I gave up on detecting the data :(
    #icmp=dpkt.icmp.ICMP.Echo(str_p.encode())
    #print(icmp.data)
   
    
    


