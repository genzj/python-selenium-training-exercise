import requests


def read_todo(limit=10):
    # Send a request to the API server and store the response.
    response = requests.get('http://jsonplaceholder.typicode.com/todos')

    # Confirm that the request-response cycle completed successfully.
    if response.ok:
        return response.json()[:limit]
    else:
        return []

