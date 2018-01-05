node {
  checkout scm

  stage('Install') {
    parallel 3.5.4: {
        sh './jenkins.sh -p 3.5.4 install'
    },
    3.6.4: {
        sh './jenkins.sh -p 3.6.4 install'
    }
  }
  stage('Lint') {
    parallel 3.5.4: {
        sh './jenkins.sh -p 3.5.4 lint'
    },
    3.6.4: {
        sh './jenkins.sh -p 3.6.4 lint'
    }
  }
  stage('test') {
    parallel 3.5.4: {
        sh './jenkins.sh -p 3.5.4 test'
    },
    3.6.4: {
        sh './jenkins.sh -p 3.6.4 test'
    }
  }
}
