#!/usr/bin/env python

#Python script to decode the BigIp cookie 
#OnlyForPentesters
#BigIP cookies example string: 3160599386.36195.0000

import struct
import sys

bigipcookie = sys.argv[1]
print "\n[+] BigIP Cookie to decode: %s[+] \n" % bigipcookie

(host, port, end) = bigipcookie.split('.')

(a, b, c, d) = [ord(i) for i in struct.pack("<I", int(host))]

(e) = [ord(e) for e in struct.pack("<H", int(port))]
port = "0x%02X%02X" % (e[0],e[1])

print "\n[+] Decoded Host and Port Value: %s.%s.%s.%s:%s [+]" % (a,b,c,d, int(port,16))
print "[+]OnlyForPentesters[+]\n \n"
