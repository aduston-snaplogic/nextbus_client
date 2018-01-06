pipeline {
  agent none
  stages {
    stage('Install with Python 3.5') {
      steps {
        sh './jenkins.sh -p 3.5.4 install'
      }
    }
    stage('Lint with Python 3.5') {
      steps {
        sh './jenkins.sh -p 3.5.4 lint'
      }
    }
    stage('Test with Python 3.5') {
      steps {
        sh './jenkins.sh -p 3.5.4 install'
      }
    }
    stage('Install with Python 3.6') {
      steps {
        sh './jenkins.sh -p 3.6.4 install'
      }
    }
    stage('Lint with Python 3.6') {
      steps {
        sh './jenkins.sh -p 3.6.4 lint'
      }
    }
    stage('Test with Python 3.6') {
      steps {
        sh './jenkins.sh -p 3.6.4 install'
      }
    }
  }
}