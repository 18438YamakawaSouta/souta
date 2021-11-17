from abc import abstractclassmethod
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as A:
 A.bind(('0.0.0.0', 50007))
 while True:
     B, ad = A.recvfrom(1024)
     print("data: {}, addr: {}".format(B, ad))