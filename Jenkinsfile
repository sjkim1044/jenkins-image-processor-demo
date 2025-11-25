pipeline {
    agent any

    environment {
        IMAGE_NAME = "image-processor"
        CONTAINER_NAME = "image-processor"
    }

    stages {

        stage('Build Docker image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Run container') {
            steps {
                sh """
                docker rm -f ${CONTAINER_NAME} 2>/dev/null || true
                docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                """
            }
        }
    }
}
