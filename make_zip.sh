#!/bin/bash

PROJECT_HOME=`pwd`
WORK_DIR=${PROJECT_HOME}/work
WORK_APP=${PROJECT_HOME}/work/app

if [ -d ${WORK_APP} ]; then
    rm -rf ${WORK_APP}
fi 
if [ -d ${WORK_DIR}/app.zip ]; then
    rm ${WORK_DIR}/app.zip
fi

cp -r ${PROJECT_HOME}/app ${WORK_APP}

rm -rf ${WORK_APP}/config/.aws

echo /dev/null > ${WORK_APP}/log/app.log

rm -rf ${WORK_APP}/src/__pycache__
rm ${WORK_APP}/src/sample.env
rm ${WORK_APP}/start.sh

cd ${WORK_DIR}
zip -r app.zip ./app

rm -rf ${WORK_APP}

cd ${PROJECT_HOME}