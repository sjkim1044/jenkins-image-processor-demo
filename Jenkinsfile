pipeline {
    agent any

    environment {
        IMAGE_NAME     = "flask-demo"
        CONTAINER_NAME = "flask-demo"
        HOST_PORT      = "8082"
        CONTAINER_PORT = "5000"
    }

    stages {
        stage('Build Docker image') {
            steps {
                sh '''
                  echo "== Docker 이미지 빌드: ${IMAGE_NAME}:${BUILD_NUMBER} =="

                  docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .

                  echo "== latest 태그 갱신 =="
                  docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Run container') {
            steps {
                sh '''
                  echo "== 기존 컨테이너 정리 =="
                  docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

                  echo "== 새 컨테이너 실행 (${HOST_PORT} -> ${CONTAINER_PORT}) =="
                  docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}:latest

                  echo "== 실행 중 컨테이너 확인 =="
                  docker ps | grep ${CONTAINER_NAME} || true
                '''
            }
        }
    }
}