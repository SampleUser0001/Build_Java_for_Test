#!/bin/bash

PROJECT_HOME=`pwd`
WORK_DIR=${PROJECT_HOME}/work
WORK_APP=${PROJECT_HOME}/work/app

if [ -d ${WORK_APP} ]; then
    rm -rf ${WORK_APP}
fi 
cp -r ${PROJECT_HOME}/app ${WORK_APP}

rm -rf ${WORK_APP}/config/.aws

echo /dev/null > ${WORK_APP}/log/app.log

rm -rf ${WORK_APP}/src/__pycache__
rm ${WORK_APP}/src/sample.env
rm ${WORK_APP}/start.sh

zip ${WORK_DIR}/app.zip ${WORK_APP}

rm -rf ${WORK_APP}

cd ${PROJECT_HOME}