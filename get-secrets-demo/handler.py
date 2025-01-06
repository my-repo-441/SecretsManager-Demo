import boto3
import os
import json

def get_secret(event, context):
    secret_name = os.environ['SECRET_NAME']
    region_name = os.environ.get('AWS_REGION', 'ap-northeast-1')

    # Secrets Manager クライアントの作成
    client = boto3.client('secretsmanager', region_name=region_name)

    try:
        # Secrets Manager からシークレットを取得
        response = client.get_secret_value(SecretId=secret_name)
        
        # シークレットが JSON 形式の場合の処理
        if 'SecretString' in response:
            secret = json.loads(response['SecretString'])
        else:
            secret = response['SecretBinary']

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Secret retrieved successfully.",
                "secret": secret
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error retrieving secret.",
                "error": str(e)
            })
        }
