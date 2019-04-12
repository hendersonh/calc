
pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'mycalc add 10 10'
            }
        }
    }
}
