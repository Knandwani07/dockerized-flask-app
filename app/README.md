## Flask Application

This directory contains the source code, dependencies, templates, and application data required to run the Flask web application.

### 📂 Project Structure

```text
app/
│
├── app.py
├── visits.txt
├── requirements.txt
│
└── templates/
    └── index.html
````

### 📄 File Description

| File / Directory       | Description                                                                      |
| ---------------------- | -------------------------------------------------------------------------------- |
| `app.py`               | Contains the Flask application logic and handles incoming web requests.          |
| `visits.txt`           | Stores the current page visit count used by the Flask application.               |
| `requirements.txt`     | Defines the Python dependencies required to run the Flask application.           |
| `templates/`           | Contains the HTML templates used by Flask to generate web pages.                 |
| `templates/index.html` | Defines the web page displayed to users and renders the visit count dynamically. |

### 🔄 Application Flow

```text
Browser
   │
   │ HTTP Request
   ▼
app.py
   │
   ├── Reads visits.txt
   │
   ├── Updates visit count
   │
   ▼
templates/index.html
   │
   │ Rendered HTML
   ▼
Browser
```

### 🐍 Flask Application

The `app.py` file is the main entry point of the application.

It:

* Creates the Flask application.
* Handles requests to the `/` route.
* Reads the current value from `visits.txt`.
* Increments the visit counter.
* Renders `index.html`.
* Returns the generated HTML response to the browser.

### 📦 Dependencies

The `requirements.txt` file contains the Python packages required by the application.

These dependencies are installed during the Docker image build process.

### 🌐 HTML Template

The `templates/index.html` file contains the user interface displayed in the browser.

Flask uses the **Jinja2 templating engine** to dynamically insert the current visit count into the HTML page.

### 💾 Visit Counter

The `visits.txt` file provides simple file-based storage for the visitor counter.

The value is updated whenever the application receives a page request.

### 📝 Note

The files in this directory are copied into the Docker image during the build process and are used by the Flask application when the container starts.
