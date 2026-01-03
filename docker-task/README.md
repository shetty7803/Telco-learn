# Docker & Kubernetes Hands-on Tasks

This repository demonstrates two core container orchestration concepts:

- **Task 1:** Live editing of static web content using Docker bind mounts  
- **Task 2:** Deploying an application in Kubernetes and exposing it using a NodePort Service  

These tasks are commonly used in cloud, VNF, and Kubernetes practical assessments.

---

## Task 1: Editing Static Page Content without Rebuilding Image

### Objective
Demonstrate how static web content running inside a Docker container can be updated **without rebuilding the image**, using a **bind mount**.

This approach is useful during development and testing of containerized VNFs.

---

### Steps Performed

#### 1. Create a local directory for web content
```bash
mkdir web
cd web
```

#### 2. Create an HTML file
```bash
nano index.html
```

The file contains a static webpage served by the container.

---

#### 3. Run Nginx container using a bind mount
```bash
docker run -d \
  --name vnf-web \
  -p 8080:80 \
  -v $(pwd):/usr/share/nginx/html \
  nginx
```

**Explanation:**
- `-d` → Runs the container in detached mode  
- `-p 8080:80` → Maps host port 8080 to container port 80  
- `-v $(pwd):/usr/share/nginx/html` → Bind mounts the host directory into the container  
- `nginx` → Web server image  

---

#### 4. Access the application
Open a browser and navigate to:
```
http://localhost:8080
```

The webpage is served directly from the host directory.

---

#### 5. Edit the HTML file locally (no rebuild)
```bash
nano index.html
```

Save the file and refresh the browser.

✔ Changes appear instantly  
✔ Container is not restarted  
✔ Image is not rebuilt  

---

### Key Concepts Explained

**COPY vs Bind Mount**
- `COPY` embeds files into the Docker image and requires rebuilding for changes  
- Bind mounts reference host files directly, enabling live updates  

**Why Live Editing is Useful**
- Faster development cycles  
- Easier debugging  
- Common during VNF testing and configuration tuning  

**Trade-off**
- Bind mounts provide flexibility but reduce immutability  
- Production environments prefer immutable images  

---

## Task 2: Deployment and NodePort Service (Kubernetes)

### Objective
Deploy a web application using a Kubernetes Deployment and expose it externally using a **NodePort Service**.

---

### YAML Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodeport-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nodeport-demo
  template:
    metadata:
      labels:
        app: nodeport-demo
    spec:
      containers:
      - name: web
        image: httpd
---
apiVersion: v1
kind: Service
metadata:
  name: nodeport-demo-svc
spec:
  type: NodePort
  selector:
    app: nodeport-demo
  ports:
  - port: 80
    targetPort: 80
```

---

### Steps Performed

#### 1. Deploy the resources
```bash
kubectl apply -f nodeport.yaml
```

Verify:
```bash
kubectl get pods
kubectl get svc
```

---

#### 2. Retrieve the NodePort
```bash
kubectl get svc nodeport-demo-svc
```

Example output:
```
80:31245/TCP
```

Here, `31245` is the NodePort assigned by Kubernetes.

---

#### 3. Access the application
Open browser:
```
http://<Node-IP>:31245
```

The Apache default webpage should appear.

---

### ClusterIP vs NodePort

| Feature | ClusterIP | NodePort |
|-------|-----------|----------|
| Access scope | Internal only | External |
| IP used | Cluster IP | Node IP |
| Port range | Service port | 30000–32767 |
| Use case | Internal services | Testing / demos |

---

## Summary

- Task 1 demonstrates live content updates using Docker bind mounts  
- Task 2 demonstrates Kubernetes service exposure using NodePort  
- Both tasks highlight key container orchestration concepts used in VNFs and cloud-native applications  

---

## Author
Hands-on Docker & Kubernetes Practice
