import os

raw = input("Enter the Service name: ")
s='systemctl is-active ' + raw.strip() 
status = os.system(s)
print(status)