
pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh "mycalc sub -n 100 50" 
                sh 'pytest -v'
            }
        }
    }
}
