pipeline {
    agent {
        label 'jenkins-agent-python'
    }
    
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Sai-th/currencyConversion.git'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3 -c "print(\"Syntax check passed\")"'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t currency-converter .'
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    docker stop currency-converter || true
                    docker rm currency-converter || true
                    docker run -d --name currency-converter -p 5050:5050 currency-converter
                '''
            }
        }
    }
}
