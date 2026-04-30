#!/bin/sh

echo "[*] Starting setup..."
sleep 1

INSTALL_DIR="$HOME/.demo_tool"
BIN_DIR="$INSTALL_DIR/bin"

mkdir -p "$BIN_DIR"

cat << 'EOF' > "$BIN_DIR/demo"
#!/bin/sh
echo "Demo tool executed successfully."
EOF

chmod +x "$BIN_DIR/demo"

echo
echo "[+] Installed to $INSTALL_DIR"
echo "[i] To run: $BIN_DIR/demo"
echo
echo "Installation completed."