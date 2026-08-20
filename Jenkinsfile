pipeline {
    agent any

    environment {
    AWS_REGION = 'ap-south-1'

    BACKEND_ECR = '201173334450.dkr.ecr.ap-south-1.amazonaws.com/llm-backend'
    FRONTEND_ECR = '201173334450.dkr.ecr.ap-south-1.amazonaws.com/llm-frontend'

    IMAGE_TAG = "${BUILD_NUMBER}"
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
  			-t $BACKEND_ECR:$IMAGE_TAG \
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
                   docker push $BACKEND_ECR:$IMAGE_TAG                '''
            }
        }
	stage('Build Frontend Image') {
    	   steps {
               sh '''
           	 docker build \
              	-t $FRONTEND_ECR:$IMAGE_TAG \
             	 ./frontend
       		 '''
    }
}
	stage('Push Frontend Image') {
 	   steps {
        	sh '''
            	    docker push $FRONTEND_ECR:$IMAGE_TAG
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
			--atomic \
 		        --timeout 5m
       		     '''
    }
}
	stage('Verify Deployment') {
  	  steps {
        	sh '''
            		kubectl rollout status deployment/llm-backend --timeout=180s
            		kubectl rollout status deployment/llm-frontend --timeout=180s

           		 kubectl get pods
        	 '''
    }
}
}
}
