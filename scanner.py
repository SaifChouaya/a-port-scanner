import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
    except socket.gaierror as e:
        print(f"Error: {e}")
        sys.exit(1)
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit(1)

# Add a banner
print('-' * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print('-' * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # Returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit(1)
except socket.error:
    print("Couldn't connect to server")
    sys.exit(1)
