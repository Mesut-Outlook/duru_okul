import sys
import os
import json
import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/score':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                # Add metadata
                client_ip = self.client_address[0]
                received_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data['client_ip'] = client_ip
                data['received_at'] = received_at
                
                # Write to scores.json file in the workspace
                scores_file = os.path.join(os.path.dirname(__file__), 'scores.json')
                
                scores = []
                if os.path.exists(scores_file):
                    try:
                        with open(scores_file, 'r', encoding='utf-8') as f:
                            scores = json.load(f)
                            if not isinstance(scores, list):
                                scores = []
                    except Exception:
                        scores = []
                
                scores.append(data)
                
                with open(scores_file, 'w', encoding='utf-8') as f:
                    json.dump(scores, f, indent=2, ensure_ascii=False)
                
                # Write to human-readable log
                log_file = os.path.join(os.path.dirname(__file__), 'scores_log.txt')
                
                key = data.get('key', '')
                val = data.get('val', {})
                timestamp = data.get('received_at', '')
                
                summary = f"[{timestamp}] IP: {client_ip} | Key: {key}\n"
                
                # Try parsing the history entry (exams) or points (general)
                if isinstance(val, dict) and 'history' in val:
                    history = val['history']
                    if history and isinstance(history, list):
                        last_attempt = history[0]
                        summary += f"  📝 EXAM DONE: {last_attempt.get('examTitel', '')} | Score: {last_attempt.get('pct', 0)}% ({last_attempt.get('goed', 0)}/{last_attempt.get('totaal', 0)} correct)\n"
                elif isinstance(val, dict) and 'beste' in val:
                    summary += f"  🏆 BEST SCORES UPDATED: {json.dumps(val.get('beste', {}))}\n"
                elif isinstance(val, dict) and 'pts' in val:
                    summary += f"  💎 POINTS/XP UPDATE: {val.get('pts', 0)} XP | Badges: {len(val.get('badges', []))}\n"
                elif isinstance(val, list) and len(val) > 0 and isinstance(val[0], dict) and 'examTitel' in val[0]:
                    # Nederlands begrijpend lezen list format
                    last_attempt = val[0]
                    summary += f"  📖 READING COMPREHENSION: {last_attempt.get('examTitel', '')} | Score: {last_attempt.get('pct', 0)}% ({last_attempt.get('goed', 0)}/{last_attempt.get('totaal', 0)} correct)\n"
                else:
                    summary += f"  💾 DATA: {json.dumps(val)}\n"
                
                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(summary + "\n")
                
                # Print to stdout immediately (unbuffered print)
                print(summary, end="", flush=True)
                
                # Send 200 OK
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "success"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                return
            except Exception as e:
                print(f"Error handling /api/score: {e}", flush=True)
                self.send_response(500)
                self.end_headers()
                return
                
        # If not /api/score, do regular post 404
        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/api/score'):
            scores_file = os.path.join(os.path.dirname(__file__), 'scores.json')
            if os.path.exists(scores_file):
                try:
                    with open(scores_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                    self.send_header('Pragma', 'no-cache')
                    self.send_header('Expires', '0')
                    self.end_headers()
                    self.wfile.write(json.dumps(data).encode('utf-8'))
                    return
                except Exception as e:
                    print(f"Error reading scores: {e}", flush=True)
                    self.send_response(500)
                    self.end_headers()
                    return
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Pragma', 'no-cache')
                self.send_header('Expires', '0')
                self.end_headers()
                self.wfile.write(b"[]")
                return

        super().do_GET()

    def end_headers(self):
        # Enable CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
        
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def run(port=8125):
    # Change working directory to the directory of this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server_address = ('0.0.0.0', port)
    
    # We subclass simple HTTP handler which automatically handles GET requests
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"======================================================", flush=True)
    print(f"🏫 Duru's School Custom Server listening on port {port}...", flush=True)
    print(f"======================================================", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.", flush=True)

if __name__ == '__main__':
    port = 8125
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run(port)
