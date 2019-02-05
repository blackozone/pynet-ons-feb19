#! /usr/bin/env python
ip_address = input ("Please submit an IP Address: ")
ip_address = ip_address.split(".")
print("{:<12}{:<12}{:<12}{:<12}".format(*ip_address))

