import boto3
import os
from openai import OpenAI
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # AWS Secrets Manager から OpenAI の API キーを取得
    secret_name = os.environ['SECRET_NAME']
    region_name = os.environ.get('AWS_REGION', 'ap-northeast-1')

    # Secrets Manager クライアントの作成
    client = boto3.client('secretsmanager', region_name=region_name)
    logger.info(f"secret value:{client}")
    try:
        secret_response = client.get_secret_value(SecretId=secret_name)
        # シークレットが JSON 形式の場合の処理
        if 'SecretString' in secret_response:
            secret = json.loads(secret_response['SecretString'])
        else:
            secret = secret_response['SecretBinary']

        logger.info(f"secret value: {secret}")

        OPENAI_API_KEY = secret['OPENAI_API_KEY']
        logger.info(f"Successfully retrieved API key: {OPENAI_API_KEY}")
        client = OpenAI(
            api_key = OPENAI_API_KEY
        )

    except Exception as e:
        logger.error("Failed to call OpenAI API: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to retrieve API key.", "details": str(e)})
        }

    try:
        body = json.loads(event['body'])
        prompt = body.get('prompt', '')

        system_message = (
            "プロンプトの内容を元に返信してください。"
        )
        user_content = f"プロンプト: {prompt}"

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content},
        ]


        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=150
        )
        print(response.choices[0].message.content.strip())

        return {
            "statusCode": 200,
            "body": json.dumps({"message": response.choices[0].message.content.strip()})
        }
    except Exception as e:
        logger.error("Failed to call OpenAI API: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to call OpenAI API.", "details": str(e)})
        }
