pipeline {

    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        ACCOUNT_ID = '042729137733'

        IMAGE_NAME = 'python-web-app'
        IMAGE_TAG = "${BUILD_NUMBER}"

        REPOSITORY = "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${IMAGE_NAME}"

        SERVER = '13.207.239.166'
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build \
                -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Login to Amazon ECR') {
            steps {
                sh """
                aws ecr get-login-password --region ${AWS_REGION} | \
                docker login \
                --username AWS \
                --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                """
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh """
                docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REPOSITORY}:${IMAGE_TAG}

                docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REPOSITORY}:latest
                """
            }
        }

        stage('Push Image to Amazon ECR') {
            steps {
                sh """
                docker push ${REPOSITORY}:${IMAGE_TAG}
                docker push ${REPOSITORY}:latest
                """
            }
        }

        stage('Deploy to Application EC2') {

            steps {

                sshagent(credentials: ['application-server']) {

                    sh """
                    ssh -o StrictHostKeyChecking=no ec2-user@${SERVER} '

                    aws ecr get-login-password --region ${AWS_REGION} | \
                    docker login \
                    --username AWS \
                    --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

                    docker pull ${REPOSITORY}:latest

                    docker stop python-web-app || true

                    docker rm python-web-app || true

                    docker image prune -f

                    docker run -d \
                        --name python-web-app \
                        --restart always \
                        -p 9999:9999 \
                        ${REPOSITORY}:latest

                    docker ps

                    '
                    """
                }
            }
        }

        stage('Deployment Verification') {
            steps {
                sh """
                curl -I http://${SERVER}:9999 || true
                """
            }
        }

    }

    post {

        success {

            echo "========================================="
            echo "BUILD SUCCESSFUL"
            echo "Python Application Successfully Deployed"
            echo "Application URL : http://${SERVER}:9999"
            echo "========================================="
        }

        failure {

            echo "========================================="
            echo "BUILD FAILED"
            echo "Please check Jenkins Console Output"
            echo "========================================="
        }

        always {
            cleanWs()
        }
    }
}
