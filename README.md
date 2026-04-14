cd ~/tempbox-devops-project
cat > README.md << 'EOF'
# 🌡️ TempBox - Temperature Data Aggregation API

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://jenkins.io/)
[![AWS](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/ec2/)
[![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white)](https://helm.sh/)
[![Trivy](https://img.shields.io/badge/Trivy-1900FF?style=for-the-badge&logo=trivy&logoColor=white)](https://trivy.dev/)

## 📌 Overview

**TempBox** is a production-grade Temperature Data Aggregation API built as a complete **DevOps learning project**. It fetches real-time temperature data from IoT sensors (openSenseMap) and demonstrates a full CI/CD pipeline with industry-standard DevOps tools.

### 🎯 Project Goals

- ✅ Build a REST API with Flask
- ✅ Containerize with Docker
- ✅ Set up CI/CD with Jenkins
- ✅ Deploy to AWS EC2
- ✅ Orchestrate with Kubernetes (k3s)
- ✅ Package with Helm
- ✅ Scan security with Trivy
- ✅ Monitor with Prometheus & Grafana

## 🏗️ Architecture
────────────────────────────────────────────────────────────┐
│ AWS EC2 Instance │
│ 65.2.81.131 │
├─────────────────────────────────────────────────────────────┤
│ │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │
│ │ Docker │ │ Jenkins │ │ k3s │ │
│ │ TempBox │ │ :8080 │ │ Kubernetes │ │
│ │ :5000 │ │ │ │ │ │
│ └─────────────┘ └─────────────┘ └─────────────┘ │
│ │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │
│ │ Trivy │ │ Helm │ │ Prometheus │ │
│ │ Security │ │ Package │ │ :9090 │ │
│ └─────────────┘ └─────────────┘ └─────────────┘ │
│ │
└─────────────────────────────────────────────────────────────┘
│
▼
🌐 Public Access URLs
http://65.2.81.131:5000/health
http://65.2.81.131:8080 (Jenkins)

text

## 🚀 API Endpoints

| Method | Endpoint | Description | Example Response |
|--------|----------|-------------|------------------|
| `GET` | `/health` | Health check | `{"status":"healthy","app":"TempBox"}` |
| `GET` | `/version` | App version | `{"app":"TempBox","version":"1.0.0"}` |
| `GET` | `/temperature` | Avg temperature from IoT sensors | `{"average_temperature_c":13.27,"sensors_queried":3}` |

### Quick Test

```bash
# Health check
curl http://localhost:5000/health

# Get temperature data
curl http://localhost:5000/temperature

# Check version
curl http://localhost:5000/version
🛠️ Tech Stack
Category	Tools
Language	Python 3.11
Framework	Flask
Containerization	Docker, Docker Compose
Orchestration	Kubernetes (k3s)
CI/CD	Jenkins
Package Manager	Helm
Security	Trivy
Cloud	AWS EC2
Monitoring	Prometheus, Grafana
Version Control	Git, GitHub
📦 Local Development
Prerequisites
bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app/main.py
Docker Build
bash
# Build image
docker build -t tempbox:latest .

# Run container
docker run -d -p 5000:5000 --name tempbox-app tempbox:latest

# Test
curl http://localhost:5000/health
Docker Compose
bash
# Start all services
docker-compose up -d

# Stop services
docker-compose down
☸️ Kubernetes Deployment
Deploy with kubectl
bash
# Create namespace
kubectl create namespace tempbox

# Apply manifests
kubectl apply -f k8s/ -n tempbox

# Check status
kubectl get pods -n tempbox
kubectl get svc -n tempbox
Deploy with Helm
bash
# Install Helm chart
helm install tempbox ./helm-chart --namespace tempbox

# Upgrade deployment
helm upgrade tempbox ./helm-chart --set replicaCount=3

# Uninstall
helm uninstall tempbox -n tempbox
🔐 Security Scanning with Trivy
bash
# Scan Docker image
trivy image tempbox:latest --severity HIGH,CRITICAL

# Scan filesystem
trivy fs --severity HIGH,CRITICAL .
🔧 Jenkins CI/CD Pipeline
The Jenkinsfile defines the complete CI/CD pipeline:

groovy
stages {
    stage('Checkout')     // Pull code from GitHub
    stage('Security Scan') // Trivy vulnerability scan
    stage('Docker Build')  // Build container image
    stage('Deploy')        // Deploy to Kubernetes/Docker
    stage('Verify')        // Health check validation
}
Setup Jenkins
Access Jenkins: http://65.2.81.131:8080

Initial password: sudo cat /var/lib/jenkins/secrets/initialAdminPassword

Install suggested plugins

Create pipeline job pointing to GitHub repo

🌐 AWS EC2 Deployment
Security Group Rules
Port	Purpose
22	SSH access
80	HTTP traffic
443	HTTPS traffic
5000	TempBox API
8080	Jenkins
30000-32767	Kubernetes NodePort
9090	Prometheus
3000	Grafana
Deployment Commands
bash
# SSH into EC2
ssh -i tempbox-key.pem ubuntu@65.2.81.131

# Clone repository
git clone https://github.com/vibhakar246/tempbox-devops-project.git
cd tempbox-devops-project

# Deploy with Docker
docker build -t tempbox:latest .
docker run -d -p 5000:5000 --name tempbox-app tempbox:latest
📊 Monitoring Stack
Prometheus
bash
# Access Prometheus
http://65.2.81.131:9090
Grafana
bash
# Access Grafana
http://65.2.81.131:3000
# Default login: admin / prom-operator
📁 Project Structure
text
tempbox-devops-project/
├── app/
│   └── main.py              # Flask API application
├── k8s/
│   ├── namespace.yaml       # Kubernetes namespace
│   ├── deployment.yaml      # Deployment manifest
│   ├── service.yaml         # Service manifest
│   ├── configmap.yaml       # Configuration
│   └── hpa.yaml             # Horizontal Pod Autoscaler
├── helm-chart/
│   ├── Chart.yaml           # Helm chart metadata
│   ├── values.yaml          # Helm values
│   └── templates/           # Kubernetes templates
├── monitoring/
│   ├── prometheus.yml       # Prometheus config
│   └── grafana-datasources.yml
├── Dockerfile               # Container definition
├── docker-compose.yml       # Local development
├── Jenkinsfile              # CI/CD pipeline
├── requirements.txt         # Python dependencies
└── README.md               # This file
🧪 Testing
Unit Tests
bash
# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=app --cov-report=html
API Tests
bash
# Health endpoint
curl http://localhost:5000/health

# Temperature data
curl http://localhost:5000/temperature
🔄 CI/CD Pipeline Flow
text
GitHub Push → Jenkins Webhook → Build Triggered
                                    ↓
                            Trivy Security Scan
                                    ↓
                            Docker Image Build
                                    ↓
                            Push to Registry (ECR)
                                    ↓
                            Deploy to Kubernetes
                                    ↓
                            Health Check Verification
                                    ↓
                            ✅ Deployment Complete
📈 Monitoring & Alerting
Metrics: Prometheus collects container metrics

Dashboards: Grafana visualizes API performance

Health Checks: Kubernetes liveness/readiness probes

Logs: Docker logs and kubectl logs
