# Dockerizing a Flask Web Application with Docker 🐳

## 📖 About this Project

This project demonstrates the complete Docker containerization workflow by packaging a Python Flask web application with Docker. It covers the essential Docker concepts required to build, deploy, verify, and manage a containerized Python application in a consistent and portable environment.

The application is packaged into a custom Docker image using a Dockerfile and deployed as a Docker container running the Flask web server. Docker's port mapping feature exposes the application to the host machine, allowing users to access it through a web browser. The Flask application also implements a simple file-based visit counter that tracks page visits using `visits.txt`.

Throughout the project, you'll learn how to build Docker images, manage Python dependencies, run containers, inspect application logs, access the running application, and manage the complete Docker container lifecycle.

This project serves as a practical introduction to containerizing Python applications and provides a strong foundation for learning advanced technologies such as Docker Compose, Docker Volumes, Kubernetes, Amazon ECS, AWS Fargate, and cloud-native application deployment.

---

## 🎯 Project Objectives

- Build a custom Docker image using a Dockerfile.
- Containerize a Python Flask web application.
- Configure Python dependencies using `requirements.txt`.
- Deploy the application inside a Docker container.
- Implement a file-based page visit counter.
- Configure Docker port mapping for browser access.
- Verify container status and inspect application logs.
- Access and manage the running container using the Docker CLI.
- Manage the complete Docker container lifecycle.
- Understand the differences between Docker images and containers.
- Demonstrate practical Docker containerization best practices.

---

## 🛠️ Technologies Used

| **Technology** | **Purpose** |
| --------------------- | ----------------------------------------- |
| Docker | Containerization platform |
| Dockerfile | Defines image build instructions |
| Python | Programming language used for the application |
| Flask | Web framework used to build the application |
| Docker Container | Runs the containerized Flask application |
| Docker CLI | Builds images and manages containers |

---

## 📂 Project Structure

```text
dockerized-flask-app/
│
├── architecture-overview.md
├── cleanup-guide.md
├── deployment-guide.md
├── execution-workflow.md
│
├── app/
│   ├── app.py
│   ├── visits.txt
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```
---

## 📋 Prerequisites

Before running this project, ensure you have:

- Docker Desktop (Windows/macOS) or Docker Engine (Linux) installed.
- Docker Engine running successfully.
- Basic familiarity with the command line.
- Basic understanding of Python and Flask.
- A modern web browser.

---

## 📚 Concepts Covered

This project demonstrates practical implementation of the following Docker and application concepts:

- Docker Containerization
- Docker Images and Containers
- Dockerfile Fundamentals
- Flask Application Containerization
- Python Dependency Management
- Container Lifecycle Management
- Port Mapping

---

## 🤝 Let's Connect

- 💼 **LinkedIn:** https://www.linkedin.com/in/khushi-nandwani/
- 💻 **GitHub:** https://github.com/Knandwani07
- 📬 **Substack:** https://substack.com/@khushinandwani07
- ✍️ **Dev Community:** https://dev.to/khushi_nandwani07
- 📝 **Medium:** https://medium.com/@khushinandwanii
- 🌐 **Portfolio:** https://main.d1n4wt6uo5bfx6.amplifyapp.com/

---

⭐ **If you found this project helpful, consider giving it a star!**
