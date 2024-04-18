
class Request:
    def __init__(self, file):
        self.file = file


        self.method = ""
        self.protocol = ""
        self.uri = ""
        self.headers = {}
        self.body = None

        self.parse_request_line()
        self.parse_headers()
        self.parse_body()

    def parse_request_line(self):
        request_line = self.read_line()
        self.method, self.uri, self.protocol = request_line.split()
        _, self.uri = self.uri.split("/")


    def read_line(self):
        return self.file.readline().decode().strip()

    def parse_headers(self):
        while True:
            header = self.read_line()
            if not header:
                break
            key, value = header.split(": ")
            self.headers[key] = value
    
    def parse_body(self):
        if "Content-Length" in self.headers:
            self.body = self.file.read(int(self.headers["Content-Length"]))