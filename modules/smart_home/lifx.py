from config.config import LIFX_TOKEN
import requests

token = LIFX_TOKEN
# Authorize ourselves
headers = {
    "Authorization": "Bearer %s" % token,
}


def get_lights() -> str:
    # This is for Troubleshooting purposes
    # Get all lights
    response = requests.get("https://api.lifx.com/v1/lights/all",
                            headers=headers)
    # Make sure we got a response of 200
    if response.status_code == 200:
        lights = response.json()

        # Show what Lights we have access to
        for light in lights:
            print(f"ID: {light['id']}, Label: {light['label']},"
                  f"Power: {light['power']}, "
                  f"Brightness: {light['brightness']}, Color: {light['color']}"
                  )
    else:
        print("Error: %s" % response.status_code)
