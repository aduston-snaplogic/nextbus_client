def pythonVersions = ["3.5.4", "3.6.4"]
pipeline {
  for(int i=0; i < pythonVersions.size(); i++) {
    def pythonVersion = pythonVersions[i]
    agent {
      label "python-${pythonVersion}"
    }
    stages {
      stage("Install on Python ${pythonVersion}") {
        steps {
          sh "./jenkins.sh -p ${pythonVersion} install"
        }
      }
      stage("Lint with Python ${pythonVersion}") {
        steps {
          sh "./jenkins.sh -p ${pythonVersion} lint"
        }
      }
      stage("Test with Python ${pythonVersion}") {
        steps {
          sh './jenkins.sh -p ${pythonVersion} install'
        }
      }
    }
  }
}