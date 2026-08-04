from config.profile import PROFILE
from config.settings import APP_NAME, VERSION


def get_home():
    return {
        "application": APP_NAME,
        "version": VERSION,
        "developer": PROFILE["name"],
        "role": PROFILE["role"],
        "status": "Running",
        "message": "Welcome to my DevOps AI Portfolio API"
    }
