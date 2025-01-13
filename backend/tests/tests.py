import tests1, tests2, tests3, tests4
from requests.exceptions import ConnectionError

def parse_host_port(connection_string):
    # Extract the part of the string containing host and port
    start = connection_string.find("host='") + len("host='")
    end = connection_string.find("'", start)
    host = connection_string[start:end]
    
    start = connection_string.find("port=") + len("port=")
    end = connection_string.find(")", start)
    port = int(connection_string[start:end])
    
    return host, port

if __name__ == "__main__":
    try:
        print("Starting API tests...\n")
        tests1.main()
        tests2.main()
        tests3.main()
        tests4.main()
        print("\nAll tests passed successfully.")
    except ConnectionError as e:
        error = str(e)
        host, port = parse_host_port(error)
        print(f"Connection refused. Make sure the API is hosted at http://{host}:{port}")
        