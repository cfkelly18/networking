import dpkt
import socket


def perform_xor(message,key):
  #this function ensures they key is the right length and then performs the XOR
    if (len(key)<len(message)):
        dif=(len(message)-len(key))
       
        padding=(dif*'x')
        key=(key+padding)
       

    counter=0
    xor_string=""
    while(counter<len(message)):
        new_chr=(ord(key[counter])^ord(message[counter]))
        xor_string=(xor_string+str(new_chr))
        counter=counter+1


    print("key: " ,key)
    print("Message: ", message)
    print("XOR STRING: " ,xor_string)
    return(xor_string)

    


secret=input("Enter secret data: ")
key=input("Enter Key: ")
#using localhost for simplicity 
d_ip='127.0.0.1'


icmp_packet= dpkt.icmp.ICMP()
icmp_packet.type=8

packet_body= dpkt.icmp.ICMP.Echo()
packet_body.id=50
packet_body.seq=12

#passing the body and the key into my function to be processed and then XOR
packet_body.data=perform_xor(secret,key).encode()
icmp_packet.data=packet_body
send=(str(packet_body).encode())



the_socket=socket.socket(socket.AF_INET, socket.SOCK_RAW,dpkt.ip.IP_PROTO_ICMP)
the_socket.connect((d_ip,1))
the_socket.send(send)



