import json


def printJson(dict):
    """Prints a JSON object in a readable format.

    Args:
        obj (dict): A JSON object.
    """
    print(json.dumps(dict, indent=4, sort_keys=True))
