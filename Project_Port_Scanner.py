#This is a simple port-scanner that will scann up to 1-1025 ports.
#This port-scanner will record the start and end times of scan process.
# It will label if a port is open in clear text
#Here is my code posted in the body of the email
import socket
import sys
import subprocess
from datetime import datetime
import time

# Clear the screen
subprocess.call('clear', shell=True)

remoteServer = input('Enter a host to scan: ')
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# writing to file here
file = open("port.txt", "a+")
now = datetime.now()
print('start=', now)
file.write('\nstart=' + str(now))

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Scan beginning at: ", dt_string)
file.write(" Scan beginning at: " + str(dt_string))
# sys.stdout.close()
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port " + str(port) + " is open")
            file.write(("\nPort " + str(port) + " is open"))
        # else:
            # print("Port " + str(port) + " is closed")

        # sys.stdout.close()
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    file.write("\nYou pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    file.write('\nHostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    file.write("\nCouldn't connect to server")
    sock.settimeout(10)
    sys.exit()

start = time.time()
a = 1000
while a > 0:
    # print('#')
    a = a - 1
end = time.time()

elapsed = end - start
# sys.stdout.open()
print("Total time scanned: " + str(elapsed))
print('end=', now)
file.write("\nTotal time scanned: " + str(elapsed))
file.write(' end=' + str(now))

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Scan ended at: ", dt_string)
file.write(" Scan ended at: " + str(dt_string))
# end of writing to file here
# sys.stdout.close()
file.close()
