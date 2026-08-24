# 🚀 LLM Deployment on Amazon EKS


A production-style DevOps project demonstrating the deployment of a containerized Large Language Model (LLM) application on Amazon EKS.

The project integrates CI/CD automation, container security scanning, Kubernetes orchestration, Helm deployments, monitoring, and real-time alerting.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Cloud | AWS, Amazon EC2 |
| Kubernetes | Amazon EKS, Kubernetes, Helm |
| Containers | Docker, Amazon ECR |
| CI/CD | Jenkins |
| Security | Trivy |
| Monitoring | Prometheus, Grafana |
| Alerting | Alertmanager, Slack |
| Application | FastAPI, Streamlit |
| LLM | Ollama, TinyLlama |
| Version Control | GitHub |


## 🏗️ Architecture

```text
GitHub
   │
   ▼
Jenkins
   │
   ▼
Trivy Security Scan
   │
   ▼
Docker Build
   │
   ▼
Amazon ECR
   │
   ▼
Helm Deployment
   │
   ▼
Amazon EKS
   │
   ├── Streamlit Frontend
   ├── FastAPI Backend
   └── Ollama + TinyLlama
```

## 🖥️ LLM Application

The application consists of a Streamlit frontend, FastAPI backend, and Ollama running the TinyLlama model. Users interact with the frontend, which sends requests to the backend for LLM inference.


<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/d2bee99f-920b-4fd4-9140-b792de2400da" />

## 🔄 Jenkins CI/CD Pipeline

Jenkins automates the application deployment workflow by building Docker images, performing security scanning with Trivy, pushing images to Amazon ECR, and deploying the application to Amazon EKS using Helm. Trivy is integrated into the CI/CD pipeline to scan container images for vulnerabilities before deployment. This helps identify security issues during the application delivery process.

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/d7c04e85-a3ec-46c3-9999-5e4ea271fb67" />


## ☸️ Kubernetes Deployment

The LLM application is deployed on Amazon EKS using Kubernetes and Helm. The deployment consists of separate Pods for the backend, frontend, and Ollama services. Used RBAC for security
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/756cf3ba-d70f-43c1-9ef2-3a18b038c216" />



## 🖥️ HELM Deployment

Helm is used to package and deploy the application components to Amazon EKS. Helm templates manage the backend, frontend, and Ollama deployments and simplify application upgrades.
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/56251985-a4d6-47c5-9e51-fa756ba66c0a" />


## ⚖️ Horizontal Pod Autoscaling (HPA)

HPA was configured for the LLM backend to automatically scale Pods based on CPU utilization.

- Minimum replicas: 1
- Maximum replicas: 3
- CPU target: 70%

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/16ad6f4d-f47a-4a0a-a4f2-9b66b974a5d9" />

## 📊 Prometheus Monitoring

Prometheus is deployed in the Kubernetes cluster to collect infrastructure and workload metrics. It monitors Kubernetes components and provides metrics used for operational visibility.
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5c8ab6b1-8146-46b6-b303-b2c94b978cd8" />

## 📈 Grafana Dashboard

Grafana is used to visualize Prometheus metrics through dashboards. The dashboard provides visibility into Kubernetes workloads, including Pod status, CPU usage, memory usage, and restart counts.
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/9606c7b9-c171-4f7e-b091-1d8ccc471ba3" />


## 🚨 Alerting and Slack Notifications

Grafana Alerting and Alertmanager are configured to detect operational issues and send notifications to Slack. This provides practical experience with real-time monitoring and alerting workflows.
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/dc632079-d8fe-4735-9092-5695064e9613" />


## 🧪 Alert Testing

To validate the monitoring and alerting workflow, the backend application was intentionally scaled down.

The backend deployment was reduced to zero replicas to simulate an application outage. Prometheus and Grafana detected the backend unavailability, and the configured alert was triggered.

The alert notification was successfully delivered to the Slack monitoring channel.
```text
Backend Replicas Scaled to 0
            │
            ▼
Backend Application Unavailable
            │
            ▼
Prometheus Detects Metric Change
            │
            ▼
Grafana Alert Rule Triggers
            │
            ▼
Slack Notification Sent
```

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/1081e128-2aa1-41ba-bb47-c038a41b9a54" />

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/04fa65be-ab15-4d35-bfea-aeb7d7c24b7a" />

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/20626a4a-7248-40a2-803c-89e6d7b14002" />

## 🚀 Deployment Workflow
```text
GitHub
   │
   ▼
Jenkins Pipeline
   │
   ▼
Docker Build
   │
   ▼
Trivy Security Scan
   │
   ▼
Amazon ECR
   │
   ▼
Helm
   │
   ▼
Amazon EKS
   │
   ▼
Prometheus
   │
   ▼
Grafana
   │
   ▼
Slack Alerts
```
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5d96320d-8e0f-438d-a1d6-bbea0e6ada2a" />



## 👩‍💻 Author

Ashwini N K

AWS / DevOps Engineer

GitHub: https://github.com/nkashwini97
