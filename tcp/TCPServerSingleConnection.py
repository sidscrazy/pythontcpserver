import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.
    
    It is instantiated once per connection to the server, and overrides the
    handle() method to implement communication to the client.
    """
    def handle(self):
        while True:
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            if not self.data:
                break
            print(f"{self.client_address[0]} wrote: {self.data.decode('utf-8')}")
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

if __name__ == "__main__":
    #HOST, PORT = "localhost", 8585
    # To debug the server, replace the IP address with "localhost"
    HOST, PORT = "192.168.86.39", 8585
    
    

    # Create the server, binding to localhost on port 8585
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        print(f"Server starting on {HOST}:{PORT}")
        print(f"Clients should connect to {HOST}:{PORT}")
        print(f"This will keep running until you interrupt the program with Ctrl-C")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer is shutting down")
