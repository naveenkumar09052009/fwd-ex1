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