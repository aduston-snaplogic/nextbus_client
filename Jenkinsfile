pipeline {
  agent none
  stages {
    stage('Install') {
      parallel {
        stage('Install with Python 3.5') {
          agent {
            label "python35"
          }
          steps {
            sh './jenkins.sh -p 3.5.4 install'
          }
        }
        stage('Install with Python 3.6') {
          agent {
            label "python36"
          }
          steps {
            sh './jenkins.sh -p 3.6.4 install'
          }
        }
      }
    }
    stage('Lint') {
      parallel {
        stage('Lint with Python 3.5') {
          agent {
            label "python35"
          }
          steps {
            sh './jenkins.sh -p 3.5.4 lint'
          }
        }
        stage('Lint with Python 3.6') {
          agent {
            label "python36"
          }
          steps {
            sh './jenkins.sh -p 3.6.4 lint'
          }
        }
      }
    }
    stage('Test') {
      parallel {
        stage('Run tests with Python 3.5') {
          agent {
            label "python35"
          }
          steps {
            sh './jenkins.sh -p 3.5.4 test'
          }
        }
        stage('Run tests Python 3.6') {
          agent {
            label "python36"
          }
          steps {
            sh './jenkins.sh -p 3.6.4 test'
          }
        }
      }
    }
  }
}