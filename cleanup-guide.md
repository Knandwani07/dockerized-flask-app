# 🧹 Cleanup Guide

This guide explains how to safely stop and remove the Docker resources created for the Dockerized Flask Web Application.

---

## ⏹️ Stop the Container

Stop the running Flask container:

```bash
docker stop flask-container
````

Verify that the container has stopped:

```bash
docker ps
```

The container should no longer appear in the list of running containers.

---

## 🗑️ Remove the Container

Remove the stopped container:

```bash
docker rm flask-container
```

Verify that the container has been removed:

```bash
docker ps -a
```

---

## 🧹 Remove the Docker Image

Remove the Docker image created for the Flask application:

```bash
docker rmi flask-docker-app
```

Verify that the image has been removed:

```bash
docker images
```

---

## 📂 Remove Project Files

If you also want to remove the local project files, navigate to the parent directory:

```bash
cd ..
```

Remove the project directory:

```bash
rm -rf flask-docker-app
```

For Windows PowerShell:

```powershell
Remove-Item -Recurse -Force flask-docker-app
```

---

## ✅ Verify Cleanup

Check for remaining containers:

```bash
docker ps -a
```

Check for remaining images:

```bash
docker images
```

The Flask container and `flask-docker-app` image should no longer be present.

---

## 🎉 Cleanup Complete

All Docker resources created for the **Dockerized Flask Web Application** have been removed. The container, Docker image, and local project files have been cleaned up successfully.
