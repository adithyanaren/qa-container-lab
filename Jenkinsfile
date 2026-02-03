pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/adithyanaren/qa-container-lab.git'
            }
        }

        stage('Run Docker Tests') {
            steps {
                sh '''
                docker-compose down || true
                docker-compose up --build --abort-on-container-exit
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                allure generate allure-results --clean -o allure-report
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}
