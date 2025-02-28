Here’s a comprehensive `README.md` for your Flask debug app project. This `README.md` includes instructions for setting up the project, running it, and testing it using `uv` as the dependency solver.

---

# Flask Debug App

A Flask-based debug application that logs all incoming HTTP requests, including their method, URL, headers, arguments, and body. This app is designed to help debug and inspect HTTP requests.

---

## Features

- Logs all incoming HTTP requests (GET, POST, PUT, DELETE, etc.).
- Supports any URL path and query parameters.
- Logs request headers, arguments, form data, JSON body, and raw data.
- Returns a JSON response with all request details.
- Easy to set up and run using `uv` as the dependency solver.

---

## Prerequisites

- Python 3.7 or higher.
- `uv` installed (for dependency management).

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/flask-debug-app.git
   cd flask-debug-app
  ```

2. **Install dependencies using `uv`:**

   ```bash
   uv sync
   ```

---

## Running the App

### Using Flask Development Server

To run the app using Flask's built-in development server:

```bash
python main.py
```

The app will be available at `http://127.0.0.1:5000`.

### Using Gunicorn (Production)

To run the app using Gunicorn (recommended for production):

```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 "app.debug_app:create_app()"
```

---

## Testing the App

You can test the app using tools like `curl`, Postman, or your browser.

### Example Requests

1. **GET Request with Query Parameters:**

   ```bash
   curl "http://127.0.0.1:5000/test?param1=value1&param2=value2"
   ```

2. **POST Request with JSON Body:**

   ```bash
   curl -X POST "http://127.0.0.1:5000/test" -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}'
   ```

3. **PUT Request with Form Data:**

   ```bash
   curl -X PUT "http://127.0.0.1:5000/test" -d "param1=value1" -d "param2=value2"
   ```

4. **DELETE Request:**

   ```bash
   curl -X DELETE "http://127.0.0.1:5000/test"
   ```

---

## Running Tests

The project includes pytest tests to verify the functionality of the app.

1. **Install test dependencies:**

   ```bash
   uv sync --dev
   ```

2. **Run the tests:**

   ```bash
   uv run pytest
   ```

---

## Project Structure

```
flask-debug-app/
│
├── app/
│   └── debug_app.py          # Main Flask application
│
├── tests/
│   └── test_debug_app.py     # Test cases for the Flask app
│
├── README.md                 # Project documentation
```

---

## Dependencies

### Production Dependencies 

```
flask==3.0.0
gunicorn==21.2.0
```

### Test Dependencies

```
pytest==7.4.0
pytest-flask==1.2.0
```

---

## Logging

The app logs all incoming requests to the console. Example log output:

```
DEBUG:__main__:Request Method: POST
DEBUG:__main__:Request URL: http://127.0.0.1:5000/test
DEBUG:__main__:Request Headers: {'Host': '127.0.0.1:5000', 'User-Agent': 'curl/7.64.1', 'Accept': '*/*', 'Content-Type': 'application/json', 'Content-Length': '36'}
DEBUG:__main__:Request Args: ImmutableMultiDict([])
DEBUG:__main__:Request Form: ImmutableMultiDict([])
DEBUG:__main__:Request JSON: {'key1': 'value1', 'key2': 'value2'}
DEBUG:__main__:Request Data: {"key1": "value1", "key2": "value2"}
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Flask: https://flask.palletsprojects.com/
- Gunicorn: https://gunicorn.org/
- pytest: https://docs.pytest.org/

---

Let me know if you need further assistance! 😊
