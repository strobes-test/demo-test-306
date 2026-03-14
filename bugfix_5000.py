import requests

def fetch_http_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return {
            'Response Code': response.status_code,
            'Protocol version': response.version,
            'HTTP/2 TLS Support': 'Yes' if 'h2' in response.headers.get('Alt-Svc', '').lower() else 'No',
            'HTTP/2 Cleartext Support': 'Yes' if 'http/2' in response.headers.get('Alt-Svc', '').lower() else 'No',
            'SSL': 'Yes' if response.url.startswith('https://') else 'No',
            'Keep-Alive': 'Yes' if 'keep-alive' in response.headers.get('Connection', '').lower() else 'No',
            'Options allowed': 'Not implemented',  # As per the issue, this is not implemented
            'Headers': response.headers
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

# Test cases
def test_fetch_http_info():
    test_urls = [
        'https://www.google.com',  # This should have HTTP/2 TLS Support
        'https://example.com',    # This should not have HTTP/2 TLS Support
        'http://example.com'      # This should not have SSL
    ]

    for url in test_urls:
        print(f"Testing URL: {url}")
        result = fetch_http_info(url)
        if 'error' in result:
            print(f"Error fetching {url}: {result['error']}")
        else:
            print(result)
        print('-' * 40)

# Run test cases
test_fetch_http_info()