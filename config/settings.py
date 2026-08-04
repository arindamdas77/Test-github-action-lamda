import os

APP_NAME = "DevOps AI Portfolio"

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

VERSION = os.getenv("APP_VERSION", "1.0.0")

REGION = os.getenv("AWS_REGION", "ap-south-1")
