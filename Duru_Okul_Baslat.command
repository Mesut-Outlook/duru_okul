#!/bin/bash
# Duru's School — start de unified oefensite
# Dubbelklik dit bestand om te beginnen.

cd "$(dirname "$0")"

PORT=8125

# Submodules bijwerken zodat alle sites aanwezig zijn
echo "Submodules bijwerken..."
git submodule update --init --recursive

# Lokaal IP-adres opzoeken (voor andere computers in hetzelfde netwerk)
if command -v ipconfig >/dev/null 2>&1; then
  LANIP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)
else
  LANIP=$(ip route get 1.0.0.0 2>/dev/null | awk '{print $7}')
fi

# Zoek geschikte tool om browser te openen (macOS: open, Linux: xdg-open)
if command -v open >/dev/null 2>&1; then
  OPEN_CMD="open"
elif command -v xdg-open >/dev/null 2>&1; then
  OPEN_CMD="xdg-open"
else
  OPEN_CMD="echo"
fi

LOCAL_URL="http://localhost:$PORT/"

echo "======================================================"
echo "  🏫  Duru's School wordt gestart..."
echo "======================================================"
echo ""
echo "  Op DEZE computer:"
echo "      $LOCAL_URL"
echo ""
if [ -n "$LANIP" ]; then
  echo "  Op een ANDERE computer in hetzelfde wifi/netwerk"
  echo "  (bv. de laptop van Duru) — typ dit in de browser:"
  echo "      http://$LANIP:$PORT/"
  echo ""
fi
echo "  Laat dit venster open tijdens het oefenen."
echo "  Stoppen? Klik hier en druk op Ctrl + C."
echo "======================================================"

# Open de browser op deze computer na een korte pauze
( sleep 1; "$OPEN_CMD" "$LOCAL_URL" ) &

# Start een eenvoudige lokale webserver (luistert op alle netwerk-adressen)
if [ -f "server.py" ]; then
  if command -v python3 >/dev/null 2>&1; then
    python3 -u server.py $PORT
  elif command -v python >/dev/null 2>&1; then
    python -u server.py $PORT
  fi
elif command -v python3 >/dev/null 2>&1; then
  python3 -m http.server $PORT --bind 0.0.0.0
elif command -v python >/dev/null 2>&1; then
  python -m SimpleHTTPServer $PORT
else
  echo "Python niet gevonden. Open anders index.html direct in je browser."
  "$OPEN_CMD" "index.html"
fi
