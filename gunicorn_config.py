import multiprocessing

# Server socket
bind = "0.0.0.0:5002"
backlog = 2048

# Worker processes
workers = 4  # Fixed number of workers instead of CPU-based calculation
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Process naming
proc_name = 'file_namer_api'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None 