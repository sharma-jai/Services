import os

raw = input("Enter the Service name to check it's status: ")
s='systemctl is-active '  + raw
status = os.system(s)
print(status)
