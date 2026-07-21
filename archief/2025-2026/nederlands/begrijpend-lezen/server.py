#!/usr/bin/env python3
import http.server
import socketserver
import socket
import sys

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def get_local_ip():
    try:
        # Create a dummy connection to a public DNS server to find the interface used for routing
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "0.0.0.0"

def start_server():
    local_ip = get_local_ip()
    
    print("\n" + "="*70)
    print("🚀 MEESTER MAX - BEGRIJPEND LEZEN TRAINER NETWERK SERVER ACTIEF!")
    print("="*70)
    print(f"🔗 Bu bilgisayardan giriş:              http://localhost:{PORT}")
    if local_ip != "0.0.0.0":
        print(f"🔗 Aynı ağdaki diğer bilgisayarlardan:  http://{local_ip}:{PORT}")
    print("="*70)
    print("Kapatmak için: Ctrl + C\n")

    # Bind to 0.0.0.0 to enable incoming LAN connections
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nSunucu kapatıldı. İyi günler!")
        sys.exit(0)
    except Exception as e:
        print(f"Sunucu başlatılırken hata oluştu: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()
