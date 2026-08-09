# 🏛️ Architecture Overview

<img width="1456" height="1456" alt="image" src="https://github.com/user-attachments/assets/d56306e7-7888-4c2c-9491-089ed19a2cf6" />

The application follows a simple containerized architecture where a web browser communicates with a Flask application running inside a Docker container.

The Flask application processes incoming HTTP requests, maintains the page visit count using `visits.txt`, and dynamically renders the web page using the `index.html` Jinja2 template.

The Docker image packages the Flask application, Python runtime, dependencies, and required files into a portable environment that can be consistently deployed and executed.

---

## 🧩 Architecture Flow

- The user accesses the application through a web browser using **localhost:5000**, which sends HTTP requests to the Flask application running inside the Docker container.
- **Docker port mapping** forwards requests from host port `5000` to port `5000` inside the container.
- The **Flask application (`app.py`)** receives each request, reads and updates the visit count stored in `visits.txt`, and generates the application response.
- The **`index.html` template** located inside the `templates/` directory is rendered using Flask's Jinja2 templating engine and returned to the browser.
- The **Dockerfile** defines the container environment, installs the dependencies listed in `requirements.txt`, copies the application files, and configures the Flask application to run inside the container.
- The resulting **Docker image** provides a portable and isolated environment for running the Flask application.
