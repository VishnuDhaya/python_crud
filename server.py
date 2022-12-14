from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector
from read import read
from create import create
from update import update
from delete import delete
import logging
import json
logging.basicConfig(format = '%(asctime)s | %(filename)s: %(message)s', level = logging.NOTSET)

def db_connect():
    return mysql.connector.connect(host = "localhost", user = "devuser", password = "Passw0rd*123", database = "python_db")

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/read':

            try:
                if db_connect().is_connected():
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    # call read function from read file
                    self.wfile.write(bytes(read(db_connect()), "utf-8"))

            except mysql.connector.Error as error:

                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected: {}".format(error), "utf-8"))
            
    def do_POST(self):

        if self.path == '/create':

            try:
                if db_connect().is_connected():
                    content_length = int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body)
                    self.send_response(200)
                    self.end_headers()
                    # call create function from create file
                    self.wfile.write(bytes(create(db_connect(), req_data), "utf-8"))

            except mysql.connector.Error as error:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected: {}".format(error), "utf-8"))
                
        elif self.path == '/update':

            try:
                if db_connect().is_connected():

                    content_length = int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body)                    
                    self.send_response(200)
                    self.end_headers()
                    # call update function from update file
                    self.wfile.write(bytes(update(db_connect(), req_data), "utf-8"))

            except mysql.connector.Error as error:

                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected: {}".format(error), "utf-8"))

        elif self.path == '/delete':
            
            try:
                if db_connect().is_connected():
                    content_length = int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body) 
                    self.send_response(200)
                    self.end_headers()
                    # call delete function from delete file
                    self.wfile.write(bytes(delete(db_connect(), req_data), "utf-8"))

            except mysql.connector.Error as error:

                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected: {}".format(error), "utf-8"))


def main():
    httpd = HTTPServer(('localhost', 39000), GetHandler)
    print("Web server has been started")
    httpd.serve_forever()


if __name__ == "__main__":
    main()