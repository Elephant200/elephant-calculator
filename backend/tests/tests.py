from requests import PreparedRequest
from requests.exceptions import ConnectionError


numTests = 4

def parse_connection_error(request: PreparedRequest, error: ConnectionError):
    """
    Parse details of a failed HTTP request due to a ConnectionError.

    Args:
        request (PreparedRequest): The prepared request that caused the error.
        error (ConnectionError): The exception raised.

    Returns:
        dict: A dictionary containing:
            - url (str): The request URL.
            - method (str): The HTTP method (e.g., GET, POST).
            - headers (dict): The request headers.
            - payload (str): The request body, decoded if text or marked as binary if not text.
            - error_message (str): The error message from the exception.
    """
    parsed_details = {
        "url": request.url,
        "method": request.method,
        "headers": dict(request.headers),
        "payload": None,
        "error_message": str(error),
    }

    # Handle decoding of the payload
    if request.body:
        try:
            if isinstance(request.body, bytes):
                parsed_details["payload"] = request.body.decode("utf-8")
            else:
                parsed_details["payload"] = str(request.body)
        except UnicodeDecodeError:
            parsed_details["payload"] = "[Binary or Non-Text Data]"

    return parsed_details

def format_details(details: dict) -> str:
    """
    Formats a dictionary of details into a human-readable string.

    Args:
        details (dict): The dictionary containing the details.

    Returns:
        str: A formatted string representing the details.
    """
    formatted = []    
    for key, value in details.items():
        if isinstance(value, dict):  # For nested dictionaries (e.g., headers)
            formatted.append(f"{key.capitalize()}:")
            for sub_key, sub_value in value.items():
                formatted.append(f"  {sub_key}: {sub_value}")
        else:
            formatted.append(f"{key.capitalize()}: {value}")
    
    return "\n".join(formatted)

if __name__ == "__main__":
    for i in range(1, numTests+1):
        exec(f"import tests{i}")
    try:
        print("Starting API tests...\n")
        for i in range(1, numTests+1):
            exec(f"tests{i}.main()")
        print("\nAll tests passed successfully.")
    except ConnectionError as e:
        parsed = parse_connection_error(e.request, e)
        print(f"Connection refused. Request Details: \n{format_details(parsed)}")
        