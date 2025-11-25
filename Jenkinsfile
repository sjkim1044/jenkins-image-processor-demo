pipeline {
    agent any

    // ✅ Jenkins가 자동으로 하는 "Declarative: Checkout SCM" 끄기
    options {
        skipDefaultCheckout(true)
    }

    stages {
        // ✅ 우리가 직접 Git 체크아웃하는 단계 추가
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sjkim1044/jenkins-image-processor-demo.git',
                    credentialsId: '232cb6c4-b2a3-47c3-9b9f-3c330477cd70'
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                  IMAGE_NAME=jenkins-demo
                  IMAGE_TAG=${BUILD_NUMBER}

                  echo "== Docker 이미지 빌드: ${IMAGE_NAME}:${IMAGE_TAG} =="
                  docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

                  echo "== latest 태그 갱신 =="
                  docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Run container') {
            steps {
                sh '''
                  CONTAINER_NAME=jenkins-demo
                  IMAGE_NAME=jenkins-demo:latest

                  echo "== 기존 컨테이너 정리 =="
                  docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

                  echo "== 새 컨테이너 실행 (8081→80) =="
                  docker run -d --name ${CONTAINER_NAME} -p 8081:80 ${IMAGE_NAME}
                '''
            }
        }
    }
}
