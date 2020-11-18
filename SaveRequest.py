from http.server import BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the form data posted
        import cgi

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                print('\tReceived {!r} as {!r} ({} bytes)\n'.format(field_item.filename, field, file_len))

                # Writes the uploaded file
                with open(field_item.filename, "wb") as f:
                    f.write(file_data)
            else:
                # Regular form value
                print('\t{}={}\n'.format(field, form[field].value))

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()


if __name__ == '__main__':
    from http.server import HTTPServer

    server = HTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
