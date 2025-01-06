
# AWS Secrets ManagerのServerless Frameworkでの使用例

## プロジェクト概要
このプロジェクトは、AWS Secrets Managerに保存されたAPIキーを安全に取得して、OpenAI APIへのリクエストに使用する方法を示します。

## 関連リンク

このプロジェクトの詳細な背景や使用例については、以下のブログ記事をご覧ください：

- [AWS Secrets Managerで機密情報を守る！Serverless Frameworkでの実践例](https://www.kuretom.com/aws-secrets-manage-sls-demo/)

## 使用方法

### 前提条件
- 適切な権限で設定されたAWS CLI
- Serverless Frameworkのインストール
- Python 3.12
- AWS Secrets Managerが設定されたAWSアカウント
- AWS Secrets Managerに保存されたOpenAI APIキー

### インストール
1. リポジトリをクローン
2. `SecretsManager/get-secrets-demo`ディレクトリに移動
3. 依存関係をインストール:
   ```
   npm install
   ```

### デプロイ
Serverless Frameworkを使用してLambda関数をデプロイします:
```
serverless deploy
```

### OpenAIとの統合
取得したAPIキーを使用して、OpenAI APIへのリクエストを行うことができます。このプロジェクトには、`openai` Pythonパッケージが依存関係として含まれています。

### 設定
`serverless.yaml`ファイルには、以下の重要な設定が含まれています:
- `SECRET_NAME`: AWS Secrets Manager内の秘密情報の名前 (デフォルト: OPENAI_API_KEY)
- Secrets Managerへのアクセス権を持つIAMロールの権限

### トラブルシューティング
- AWS CLIが正しく設定され、適切な権限を持っていることを確認してください
- `serverless.yaml`内の秘密情報の名前が、Secrets Manager内の名前と一致していることを確認してください
- Lambda関数のエラーメッセージについては、CloudWatch Logsを確認してください