import json

from routes.home import get_home
from routes.profile import get_profile
from routes.skills import get_skills
from routes.projects import get_projects
from routes.health import get_health


def response(data, status=200):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(data)
    }


def lambda_handler(event, context):

    path = event.get("rawPath", "/")

    if path == "/":
        return response(get_home())

    elif path == "/profile":
        return response(get_profile())

    elif path == "/skills":
        return response(get_skills())

    elif path == "/projects":
        return response(get_projects())

    elif path == "/health":
        return response(get_health())

    else:
        return response(
            {
                "error": "Route not found"
            },
            404
        )
