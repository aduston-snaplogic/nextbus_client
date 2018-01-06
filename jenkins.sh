#!/usr/bin/env bash
#
# Script actions for running in Jenkins environment

# Set base directory location for available Python versions
PYTHON_TOOLS_DIR=${JENKINS_HOME}/tools/python
PYTHON_VERSION=3.6.4

function usage() {
    echo -e "Run the given action with the specified Python version (default is 3.6.4)\n"
    echo -e "./jenkins.sh [options] <action>"
    echo -e "\t-h --help"
    echo -e "\t--python=<version>\n"
}

function install() {
    ${PYTHON_BIN_DIR}//pip3 install -r requirements-test.txt
    ${PYTHON_BIN_DIR}/python3 setup.py install
}

function lint() {
  ${PYTHON_BIN_DIR}/python3 setup.py lint --pylint-bin=${PYTHON_BIN_DIR}/pylint
}

function run_tests() {
    ${PYTHON_BIN_DIR}/python3 setup.py test --behave-bin=${PYTHON_BIN_DIR}/behave
}

ACTION=""
while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case ${PARAM} in
        -h | --help)
            usage
            exit
            ;;
        --python)
            PYTHON_VERSION=${VALUE}
            shift
            ;;
        *)
            ACTION=${1}
            shift
            ;;
    esac
done

PYTHON_BIN_DIR=${PYTHON_TOOLS_DIR}/${PYTHON_VERSION}/bin

case ${ACTION} in
    install)
        install
        ;;
    lint)
        lint
        ;;
    test)
        run_tests
        ;;
    *)
      echo -e "Unknown action ${ACTION}\n"
      usage
      exit
      ;;
esac