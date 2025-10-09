sudo apt install python3.12-venv gunicorn


sudo python3 -m venv myenv


source myenv/bin/activate


pip install flask gunicorn



sudo nano /etc/systemd/system/signage.service


[Unit]
Description=Gunicorn service for Flask Signage App
After=network.target

[Service]
User=shecl
Group=shecl
WorkingDirectory=/home/shecl/signage
Environment="PATH=/home/shecl/signage/myenv/bin"
ExecStart=/home/shecl/signage/myenv/bin/gunicorn -b 0.0.0.0:8000 server:app
Restart=always

[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload && sudo systemctl start signage && sudo systemctl enable signage && sudo systemctl status signage
