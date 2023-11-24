def get_docs():
    """
    This function sends a GET request to the specified URL and retrieves the documentation.
    """
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs();
print(response.status_code)
#
#In this