# GetPower

## This script is very specific to get power usage from multiple cisco switches

* To use: you must specify 3 arguments
 1 the name of the file with IP's listed
 2 the username to log into the switches
 3 the password to log into the switches

The output should result in "show power inline" on each Cisco switch

### Future enhancements

* add regular expression to clean up usefull results
* add function to count types of IP phones, AP's, Cameras etc
* add summarize per switch IP to summ up total power used
* add clean report generation

## Usage example

'''
python GetPower.py IPs.txt user pass
'''

