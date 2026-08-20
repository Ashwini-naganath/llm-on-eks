pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        ECR_REPO   = '201173334450.dkr.ecr.ap-south-1.amazonaws.com/llm-backend'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ashwini-naganath/llm-on-eks.git'
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                    docker build \
                      -t $ECR_REPO:$IMAGE_TAG \
                      ./backend
                '''
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin \
                    201173334450.dkr.ecr.ap-south-1.amazonaws.com
                '''
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                    docker push $ECR_REPO:$IMAGE_TAG
                '''
            }
        }

	stage('Deploy with Helm') {
    	     steps {
       		 sh '''
            		export AWS_PAGER=""

           		 helm upgrade --install llm-rag ./helm/llm-rag \
              		--set backend.tag=$IMAGE_TAG \
              		--set frontend.tag=v2-rag
       		     '''
    }
}
	stage('Verify Deployment') {
   		 steps {
        		sh '''
           			 kubectl rollout status deployment/llm-backend --timeout=180s
            			kubectl get pods
        		   '''
   		 }
}   		 }
}
