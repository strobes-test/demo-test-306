from flask import Flask
import unittest

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

class TestFlaskApp(unittest.TestCase):
    def test_index_route(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    # Remove debug mode when deploying to production
    app.run()
```

This code removes the `debug=True` parameter from the `app.run()` call, which is not recommended for production environments. It also includes a simple test case to verify that the Flask application is running and serving the index route correctly.