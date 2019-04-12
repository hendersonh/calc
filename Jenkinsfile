
pipeline {
    agent none 
    stages {
        stage('Example Build') {
	
            agent { docker 'rackspacedot/python37' } 
            steps {
                echo 'Testing <call add> command'
                sh 'mycalc add 10 10'
            }
        }
    }
}
