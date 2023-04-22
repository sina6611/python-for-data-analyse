import requests

# Define the API endpoint URL
url = 'https://jsonplaceholder.typicode.com/todos/1'

# Make a GET request to the API endpoint
response = requests.get(url)

# Parse the JSON response into a Python dictionary object
data = response.json()

# Print the response data
print(data)
