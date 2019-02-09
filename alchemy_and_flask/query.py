import requests

from pprint import pprint


def run_query(query, headers):
    """
    A simple function to use requests.post to make the API call

    :param query: GraphQL Query String
    """

    request = requests.post(
        'http://localhost:5000/graphql',
        json={'query': query},
        headers=headers
    )
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = """
{
  allEmployees {
    edges {
      node {
        id
      }
    }
  }
}
"""


if __name__ == "__main__":
    headers = {"Authorization": "Bearer YOUR API KEY"}
    result = run_query(query, headers)  # Execute the query
    pprint(result)
