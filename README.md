# EX01 Developing a Simple Webserver
## Date:15-10-2026
## REG NO:26019228

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:~~~
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Protocols in Networking</title>
</head>
<body>

    <h1>List of Protocols in Networking</h1>

    <ul>
        <li>HTTP - Hypertext Transfer Protocol</li>
        <li>HTTPS - Hypertext Transfer Protocol Secure</li>
        <li>FTP - File Transfer Protocol</li>
        <li>SFTP - Secure File Transfer Protocol</li>
        <li>TCP - Transmission Control Protocol</li>
        <li>UDP - User Datagram Protocol</li>
        <li>IP - Internet Protocol</li>
        <li>DNS - Domain Name System</li>
        <li>DHCP - Dynamic Host Configuration Protocol</li>
        <li>SMTP - Simple Mail Transfer Protocol</li>
        <li>POP3 - Post Office Protocol Version 3</li>
        <li>IMAP - Internet Message Access Protocol</li>
        <li>SSH - Secure Shell</li>
        <li>Telnet - Teletype Network</li>
        <li>SNMP - Simple Network Management Protocol</li>
        <li>ICMP - Internet Control Message Protocol</li>
        <li>ARP - Address Resolution Protocol</li>
        <li>NTP - Network Time Protocol</li>
        <li>RDP - Remote Desktop Protocol</li>
        <li>BGP - Border Gateway Protocol</li>
    </ul>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~


## OUTPUT:
![alt text](<Screenshot (8).png>)
![alt text](<Screenshot 2026-11-14 140838.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.

