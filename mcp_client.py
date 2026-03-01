import json
import sys

def send_request(method, params):
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }
    sys.stdout.write(json.dumps(request) + "\n")
    sys.stdout.flush()
    response = sys.stdin.readline()
    return json.loads(response)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    # Prepare the request for the MCP server
    result = send_request("add_numbers", {"a": a, "b": b})
    print("Result:", result.get("result"))

if __name__ == "__main__":
    main()
