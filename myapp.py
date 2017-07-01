def app(environ, start_response):
        data = b""
        for i in range(0,100000):
        	data += b'000000001'
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
