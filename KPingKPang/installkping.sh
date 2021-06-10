#/bin/bash
if $EUID != 0; then
    echo "Se necesita sudo"
    exit 0
fi
touch /etc/systemd/system/kpingkpang.service
cat << EOF >> /etc/systemd/system/kpingkpang.service
[Unit]
Description=kpingkpang service by yukics.
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 `pwd`/kpingkpang.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable kpingkpang.service
sudo systemctl start kpingkpang.service
