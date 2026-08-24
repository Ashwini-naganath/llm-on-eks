🚀 LLM Deployment on Amazon EKS

A production-style DevOps project demonstrating the deployment of a containerized Large Language Model (LLM) application on Amazon EKS.

The project integrates CI/CD automation, container security scanning, Kubernetes orchestration, Helm deployments, monitoring, and real-time alerting.
🏗️ Architecture
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
🖥️ LLM Application

The application consists of a Streamlit frontend, FastAPI backend, and Ollama running the TinyLlama model. Users interact with the frontend, which sends requests to the backend for LLM inference.


<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/d2bee99f-920b-4fd4-9140-b792de2400da" />

🔄 Jenkins CI/CD Pipeline

Jenkins automates the application deployment workflow by building Docker images, performing security scanning with Trivy, pushing images to Amazon ECR, and deploying the application to Amazon EKS using Helm. Trivy is integrated into the CI/CD pipeline to scan container images for vulnerabilities before deployment. This helps identify security issues during the application delivery process.

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/9946068d-e833-4e8f-87cf-f0d52e28c592" />

☸️ Kubernetes Deployment

The LLM application is deployed on Amazon EKS using Kubernetes and Helm. The deployment consists of separate Pods for the backend, frontend, and Ollama services. Used RBAC for security
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/6a1e21de-6aec-4520-9f4f-c8ed756878b4" />


📦 Helm Deployment

Helm is used to package and deploy the application components to Amazon EKS. Helm templates manage the backend, frontend, and Ollama deployments and simplify application upgrades.
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/594b0acd-275a-4bb8-bdf0-3bd2139defc5" />

## ⚖️ Horizontal Pod Autoscaling (HPA)

HPA was configured for the LLM backend to automatically scale Pods based on CPU utilization.

- Minimum replicas: 1
- Maximum replicas: 3
- CPU target: 70%

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/16ad6f4d-f47a-4a0a-a4f2-9b66b974a5d9" />

📊 Prometheus Monitoring

Prometheus is deployed in the Kubernetes cluster to collect infrastructure and workload metrics. It monitors Kubernetes components and provides metrics used for operational visibility.
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5c8ab6b1-8146-46b6-b303-b2c94b978cd8" />
📈 Grafana Dashboard

Grafana is used to visualize Prometheus metrics through dashboards. The dashboard provides visibility into Kubernetes workloads, including Pod status, CPU usage, memory usage, and restart counts.
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/137925a4-38dc-4b94-8bf4-2de867d5337c" />
🚨 Alerting and Slack Notifications

Grafana Alerting and Alertmanager are configured to detect operational issues and send notifications to Slack. This provides practical experience with real-time monitoring and alerting workflows.
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/621892a2-e128-4ac8-ad79-6495e09ee714" />

🧪 Alert Testing

To validate the monitoring and alerting workflow, the backend application was intentionally scaled down.

The backend deployment was reduced to zero replicas to simulate an application outage. Prometheus and Grafana detected the backend unavailability, and the configured alert was triggered.

The alert notification was successfully delivered to the Slack monitoring channel.

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
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/1081e128-2aa1-41ba-bb47-c038a41b9a54" />

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/04fa65be-ab15-4d35-bfea-aeb7d7c24b7a" />

<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/20626a4a-7248-40a2-803c-89e6d7b14002" />

🛠️ Technology Stack
AWS
Amazon EC2
Amazon EKS
Amazon ECR
Docker
Kubernetes
Helm
Jenkins
Trivy
Prometheus
Grafana
Alertmanager
Slack
FastAPI
Streamlit
Ollama
TinyLlama
GitHub

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
<img width="979" height="552" alt="image" src="https://github.com/user-attachments/assets/5d96320d-8e0f-438d-a1d6-bbea0e6ada2a" />



👩‍💻 Author

Ashwini N K

AWS / DevOps Engineer

GitHub: https://github.com/nkashwini97
