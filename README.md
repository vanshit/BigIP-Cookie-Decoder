# BigIP-Cookie-Decoder
BigIP Cookie Decoder for Pentesters

This is a Python Script for Pentesters for quickly decoding the BigIP Cookie value to reveal the internal IP address and Port encoded within the BigIP cookie . 
The BIG-IP family of products offers the application intelligence network managers need to ensure applications are fast, secure and available. It is common to find BigIP during a pentest engagement.

The BIG-IP system uses the following address encoding algorithm to encode the IP in the cookie:
      Convert each octet value to the equivalent 1-byte hexadecimal value.
      Reverse the order of the hexadecimal bytes and concatenate to make one 4-byte hexadecimal value.
      Convert the resulting 4-byte hexadecimal value to its decimal equivalent.
The BIG-IP system uses the following port encoding algorithm:
    Convert the decimal port value to the equivalent 2-byte hexadecimal value.
    Reverse the order of the 2 hexadecimal bytes.
    Convert the resulting 2-byte hexadecimal value to its decimal equivalent.
Reference & Readmore @ https://support.f5.com/csp/article/K6917

The python script can be used to decode the cookie values and see if the internal IP Address and Port is disclosed. 
This bug can be reported during your penetests with a screenshot of Burp request and Decoded value. 
