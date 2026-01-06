"""GPU 테스트 서버 (순수 Python, 의존성 없음)"""
import http.server
import json
import subprocess

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.respond(200, {"status": "ok"})
        elif self.path == "/gpu":
            self.respond(200, self.check_gpu())
        else:
            self.respond(200, {"service": "ecs-gpu-test", "gpu": self.check_gpu()})

    def check_gpu(self):
        try:
            r = subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True)
            return {"available": r.returncode == 0, "info": r.stdout.strip() or r.stderr.strip()}
        except:
            return {"available": False, "info": "nvidia-smi not found"}

    def respond(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

print("GPU Test Server on :8080")
http.server.HTTPServer(("", 8080), Handler).serve_forever()
