pipeline {
    agent any

    stages {

        stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/swethagandham2003/enterprise-selenium-framework.git'
    }
}

        stage('Build') {
            steps {
                echo 'Building the project'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Selenium Tests'
            }
        }

        stage('Generate Report') {
            steps {
                echo 'Generating Test Report'
            }
        }
    }
}
