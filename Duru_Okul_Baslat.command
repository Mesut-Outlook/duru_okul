#!/bin/bash
# Duru's School — start de unified oefensite
# Dubbelklik dit bestand om te beginnen.

cd "$(dirname "$0")"

PORT=8125

# Submodules bijwerken zodat alle sites aanwezig zijn
echo "Submodules bijwerken..."
git submodule update --init --recursive

# Lokaal IP-adres opzoeken (voor andere computers in hetzelfde netwerk)
LANIP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)

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
( sleep 1; open "$LOCAL_URL" ) &

# Start een eenvoudige lokale webserver (luistert op alle netwerk-adressen)
if command -v python3 >/dev/null 2>&1; then
  python3 -m http.server $PORT --bind 0.0.0.0
elif command -v python >/dev/null 2>&1; then
  python -m SimpleHTTPServer $PORT
else
  echo "Python niet gevonden. Open anders index.html direct in je browser."
  open "index.html"
fi
