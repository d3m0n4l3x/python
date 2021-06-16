#!/usr/bin/python3
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

print("[+] Changeing MAC address for " + options.interface + " to " + options.new_mac)
