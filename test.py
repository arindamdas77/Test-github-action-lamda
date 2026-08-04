from app import lambda_handler


events = [
    {"rawPath": "/"},
    {"rawPath": "/profile"},
    {"rawPath": "/skills"},
    {"rawPath": "/projects"},
    {"rawPath": "/health"},
    {"rawPath": "/unknown"},
]

for event in events:
    print("=" * 60)
    print("Request:", event["rawPath"])
    print(lambda_handler(event, None))

