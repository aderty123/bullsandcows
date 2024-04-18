
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
from request import Request
from urllib.parse import parse_qs
from check import Check

check = Check()
secret_numbers = check.generate_numbers(4)
print(secret_numbers)


class HelloServerTCPHandler(StreamRequestHandler):
    def handle(self):
        request = Request(self.rfile)

        print(request.body)
        response_body = """
        <p>Can you guess 4 numbers? Enter them below separated with spaces:</p>
        <form method="POST" action="/">
            <input type="text" name="numbers"/>
            <input type="submit" value="Send"/>
        </form>
        """

        if request.method == "POST":
            request.body = request.body.decode()
            request_body = parse_qs(request.body)

            if request_body.get("numbers"):
                numbers_str = request_body["numbers"][0].split()
                response_body_check = check.validate_number(numbers_str)
                if isinstance(response_body_check, list):
                    response_body += f"<p>{check.guess_numbers(secret_numbers,numbers_str)}</p>"
                else:
                    response_body += response_body_check
            else:
                response_body += "Error"

        response_body_length = len(response_body.encode())
        response = (
            'HTTP/1.1 200 OK',
            'Content-Type: text/html',
            f'Content-Length: {response_body_length}',
            'Connection: close',
            '',
            response_body
        )

        
        self.wfile.write('\r\n'.join(response).encode())




class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    daemon_threads = True


HOST, PORT = "localhost", 8000
TCPServer.allow_reuse_address = True


with ThreadedTCPServer((HOST, PORT), HelloServerTCPHandler) as server:
    server.serve_forever()

