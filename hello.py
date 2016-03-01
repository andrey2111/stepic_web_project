def app(environ, start_response):
    body = '\n'.join(i for i in environ.get("QUERY_STRING").split('&'))
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [body]

# environ = {"QUERY_STRING": "sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8&client=ubuntu"}
# body = '\n'.join(i for i in environ.get("QUERY_STRING").split('&'))
# print(body)
