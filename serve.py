#!/usr/bin/env python3
"""Local web server for Endless Road. Sends no-cache headers and uses a fresh port every launch,
so the browser can never show an old copy of the game. Usage: python serve.py [port]"""
import http.server, os, re, socketserver, sys, threading, webbrowser

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("Pragma", "no-cache")
        super().end_headers()
    def log_message(self, *args):
        pass
    # The game photographs its own scene for the home-screen tiles and POSTs each picture here (first run, or F8 on the home screen).
    # Only the known tile names (race, free, paint, world, car_<id>) are accepted, only JPEGs, only from this page, so nothing else on disk can be touched.
    def do_POST(self):
        name = self.path.split("?")[0]
        key = name[8:]
        ok = name.startswith("/__tile/") and (key in ("race", "free", "paint", "world") or re.fullmatch(r"car_[a-z0-9]{2,8}", key) is not None)
        n = int(self.headers.get("Content-Length") or 0)
        host = self.headers.get("Host", "")
        origin = self.headers.get("Origin")
        if origin and origin.split("://", 1)[-1] != host:
            ok = False
        if not ok or n < 4 or n > 4 * 1024 * 1024:
            self.send_response(400); self.end_headers(); return
        data = self.rfile.read(n)
        if data[:3] != b"\xff\xd8\xff":
            self.send_response(400); self.end_headers(); return
        os.makedirs(os.path.join("assets", "ui"), exist_ok=True)
        tmp = os.path.join("assets", "ui", ".tile_tmp")
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, os.path.join("assets", "ui", "tile_" + key + ".jpg"))
        self.send_response(204); self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
port = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 0   # 0 = pick a free port
with socketserver.ThreadingTCPServer(("127.0.0.1", port), Handler) as srv:
    url = "http://localhost:%d/" % srv.server_address[1]
    print("Serving Endless Road at " + url + "  (press Ctrl+C or close this window to stop)")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
