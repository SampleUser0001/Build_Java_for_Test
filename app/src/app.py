# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

# import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

from factory import Boto3ClientFactory

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
    client = Boto3ClientFactory.create('codebuild')

    projectName = setting.ENV_DIC[ImportEnvKeyEnum.CODE_BUILD_NAME.value]
    logger.info("projectName : {}".format(projectName))
    response = client.start_build(
        projectName=projectName
    )
    logger.info(response)