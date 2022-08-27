# By MuZakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the REGION: ")

# this is the configration for the logger_for

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

client = boto3.client("ec2", region_name=REGION)


def del_rule(security_grp_id, rule_ids):
    try:
        res = client.revoke_security_group_ingress(
            GroupId=security_grp_id,
            SecurityGroupRuleIds=rule_ids)

    except ClientError:
        logger_for.exception('Oops sorry, Your ingress security group rule can not be deleted.')
        raise
    else:
        return res


if __name__ == '__main__':
    GROUP_ID = input("Please enter the security group id: ")
    RULE_ID = ['sgr-0059cb2f3e0311a82']
    logger_for.info(f'Please wait, we are removing a security group ingress rule(s)...')
    result = del_rule(GROUP_ID, RULE_ID)
    logger_for.info(
        f'Wow, Your security group ingress rule has been deleted: \n{json.dumps(result, indent=4)}'
    )