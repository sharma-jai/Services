import os

raw = input("Enter the Service name: ")
s='systemctl is-active '  + raw
status = os.system(s)
print(status)