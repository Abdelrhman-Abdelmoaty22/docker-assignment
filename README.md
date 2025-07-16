# 🐳 Docker Assignment – Frontend & Backend Communication

This project demonstrates how to use **Docker Compose** to run two services:
- A **Frontend Flask app** that makes a request to the backend
- A **Backend Flask app** that returns a response

Both services are containerized using Docker and communicate over a shared Docker network.

---

## 📁 Project Structure
```yaml
docker-assignment/
├── Front-End/
│ ├── DockerFile
│ └── app.py
├── Back-End/
│ ├── DockerFile
│ └── server.py
├── docker-compose.yml
```

---

## 🛠 Technologies Used

- 🐍 Python 3
- ⚙ Flask
- 🐳 Docker
- 🧱 Docker Compose

---

## 🚀 How to Run the Project

### 1 Clone the Repository
```bash
git clone https://github.com/Abdelrhman-Abdelmoaty22/docker-assignment.git
cd docker-assignment
```
### 2 Build and Start the Containers
```bash
docker-compose up --build
```
### 3. Open the Frontend in Your Browser
   Visit:
   ```arduino
   http://localhost:8080
   ```
   Expected Output:
   ```css
   Frontend talking to -> Hello from Backend!
   ```
--- 

# 🔄 How It Works
The backend runs a Flask server on port 5000 and returns a simple greeting message.

The frontend runs another Flask server (on port 8080) and makes an HTTP GET request to the backend using its Docker service name http://backend:5000.

Docker Compose connects both containers on the same network so they can communicate using service names.

---
# 🔧 Code Summary
## ✅ Front-End (Front-End/app.py)
```python
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get("http://backend:5000")
    return f"Frontend talking to -> {r.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
--- 

## 🐳 Front-End Dockerfile (Front-End/DockerFile)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask requests
CMD ["python", "app.py"]
```
--- 

## ✅ Back-End (Back-End/server.py)
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Backend!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
---

## 🐳 Back-End Dockerfile (Back-End/DockerFile)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY server.py .
RUN pip install flask
CMD ["python", "server.py"]
```
## 📦 Docker Compose File (docker-compose.yml)
```yaml
version: '3'
services:
  backend:
    build: ./Back-End
    container_name: backend
    ports:
      - "5000:5000"

  frontend:
    build: ./Front-End
    container_name: frontend
    ports:
      - "8080:5000"
    depends_on:
      - backend
```
---
# 👨‍💻 Author

**Abdelrhman Abdelmoaty**  
[GitHub Profile](https://github.com/Abdelrhman-Abdelmoaty22)

---
# 📃 License
This project is for educational purposes only. Feel free to fork and modify!

---

This is now ready to be pasted directly into your `README.md`.  
Let me know if you want to add:
- A screenshot of the output
- A GIF demo
- Badges (like build status or Python version)

I can generate those for you too 😊
