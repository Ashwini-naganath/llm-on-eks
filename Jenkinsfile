pipeline {
    agent any

    environment {
        AWS_REGION   = 'ap-south-1'
        ECR_BACKEND  = '201173334450.dkr.ecr.ap-south-1.amazonaws.com/llm-backend'
        ECR_FRONTEND = '201173334450.dkr.ecr.ap-south-1.amazonaws.com/llm-frontend'
        IMAGE_TAG    = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ashwini-naganath/llm-on-eks.git'
            }
        }

        stage('Verify Tools') {
            steps {
                sh '''
                    echo "Checking Docker..."
                    docker --version

                    echo "Checking AWS..."
                    aws --version

                    echo "Checking Helm..."
                    helm version --short

                    echo "Checking kubectl..."
                    kubectl version --client
                '''
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                    echo "Building backend image..."
                    docker build \
                      -t $ECR_BACKEND:$IMAGE_TAG \
                      ./backend

                    echo "Building frontend image..."
                    docker build \
                      -t $ECR_FRONTEND:$IMAGE_TAG \
                      ./frontend
                '''
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                    export AWS_PAGER=""

                    aws ecr get-login-password \
                      --region $AWS_REGION | \
                    docker login \
                      --username AWS \
                      --password-stdin \
                      201173334450.dkr.ecr.ap-south-1.amazonaws.com
                '''
            }
        }

        stage('Push Images') {
            steps {
                sh '''
                    echo "Pushing backend image..."
                    docker push $ECR_BACKEND:$IMAGE_TAG

                    echo "Pushing frontend image..."
                    docker push $ECR_FRONTEND:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh '''
                    export AWS_PAGER=""

                    helm upgrade --install llm-rag ./helm/llm-rag \
                      --set backend.tag=$IMAGE_TAG \
                      --set frontend.tag=$IMAGE_TAG \
                      --rollback-on-failure \
  	              --timeout 5m
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Waiting for backend rollout..."
                    kubectl rollout status deployment/llm-backend --timeout=180s

                    echo "Waiting for frontend rollout..."
                    kubectl rollout status deployment/llm-frontend --timeout=180s

                    echo "Current pods:"
                    kubectl get pods

                    echo "Backend image:"
                    kubectl get deployment llm-backend \
                      -o jsonpath='{.spec.template.spec.containers[0].image}'
                    echo

                    echo "Frontend image:"
                    kubectl get deployment llm-frontend \
                      -o jsonpath='{.spec.template.spec.containers[0].image}'
                    echo
                '''
            }

        }
	stage('Application Health Test') {
	    steps {
        	sh '''
            	echo "Testing backend application..."

            	kubectl delete pod ci-health-test --ignore-not-found=true

           	 kubectl run ci-health-test \
             	 --restart=Never \
             	 --image=curlimages/curl \
             	 -- \
             	 curl -f -sS --max-time 90 \
             	 "http://llm-backend:8000/chat?prompt=hello"

           	 kubectl wait \
              --for=jsonpath='{.status.phase}'=Succeeded \
              pod/ci-health-test \
              --timeout=120s

            kubectl logs ci-health-test

            kubectl delete pod ci-health-test --ignore-not-found=true

            echo "Application health test PASSED"
        '''
    }
}

    }

    post {
        success {
            echo "========================================="
            echo " CI/CD PIPELINE SUCCESSFUL"
            echo " Backend image: $ECR_BACKEND:$IMAGE_TAG"
            echo " Frontend image: $ECR_FRONTEND:$IMAGE_TAG"
            echo " Helm deployment: SUCCESS"
            echo "========================================="
        }

        failure {
            echo "========================================="
            echo " CI/CD PIPELINE FAILED"
            echo " Check the failed stage above."
            echo "========================================="
        }
    }
}
