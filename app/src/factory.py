# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
from enum import Enum

from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

import boto3
from boto3.session import Session

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

class Boto3ClientFactory:
    @staticmethod
    def create(service):
        credential = int(setting.ENV_DIC[ImportEnvKeyEnum.CREDENTIAL.value])
        logger.info("CREDENTIAL : {}".format(credential))
        if Credential.USE_PROFILE.value == credential:
            profile = setting.ENV_DIC[ImportEnvKeyEnum.PROFILE.value]
            logger.info("profile : {}".format(profile))
            return Session(profile_name=profile).client(service)
        elif Credential.USE_API_KEY.value == credential:
            return boto3.client(service,
                aws_access_key_id = os.environ.get(AwsApiKeyEnum.KEY.value),
                aws_secret_access_key = os.environ.get(AwsApiKeyEnum.SECRET_KEY.value),
                region_name = os.environ.get(AwsApiKeyEnum.REGION.value)
            )
        elif Credential.ON_AWS_LAMBDA.value == credential:
            # AWS Lambda用
            return boto3.client(service)
        else:
            raise AttributeError("credential is {}.".format(use_profile))

class Credential(Enum):
    USE_PROFILE=0
    USE_API_KEY=1
    ON_AWS_LAMBDA=2

class AwsApiKeyEnum(Enum):
    KEY="aws_access_key_id"
    SECRET_KEY="aws_secret_access_key"
    REGION="region"