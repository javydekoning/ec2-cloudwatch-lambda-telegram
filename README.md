## Serverless Telegram bot on AWS Lambda

### Intro
This is a simple SAM template for a Telegram chatbot written in 
Python 3 and deployed to AWS Lambda using Serverless Application
Model.

![Alt text](/screenshot.png?raw=true "Telegram screencap")

### Requirements
 1. Python 3
 2. AWS account

###
Install pip requirements:

```
pip install -r requirements.txt -t vendored
```

Testing locally:

```
echo '{"message": "Hey, this is a fake cloudwatch message!" }' | sam local invoke "hello"
```

Deploy to AWS:

```
sam package --template-file template.yaml --s3-bucket <S3 Bucket Name> --output-template-file packaged.yaml --debug
sam deploy --template-file packaged.yaml --stack-name 'lambda-telegram' --capabilities CAPABILITY_IAM
```

### P.S. 
If you need more complex solution, take a look on this example: https://github.com/Andrii-D/telegram-stepfunctions-bot/
