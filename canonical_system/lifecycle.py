
from logger import log

def startup(name, version):
    log("INFO", f"Startup: {name} v{version}")

def shutdown(name):
    log("INFO", f"Shutdown: {name}")
