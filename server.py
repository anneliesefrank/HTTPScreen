from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import codecs
from subprocess import call
from subprocess import Popen
import mpv

main = codecs.open("main.html", 'r', 'utf-8').read()

hostName = "0.0.0.0"
hostPort = 8888

player = mpv.MPV(ytdl=True)

def ytLink(number):
    yt = ['https://www.youtube.com/watch?v=xxG2UWhvXJI', 'https://youtu.be/LO2RPDZkY88', 'https://youtu.be/jbt6UWc1ZKo', 'https://youtu.be/WC5FdFlUcl0']
    intNum = int(number[1])
    return(yt[intNum])


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(main, "utf-8"))
    def do_POST(self):
        choice = ytLink(self.path)
        print(choice)
        # p = Popen(['mpv', choice])
        player.play(choice)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>This is a POST REQUEST.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
