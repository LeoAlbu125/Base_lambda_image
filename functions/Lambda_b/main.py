def lambda_handler(event, context):
    print("Hello, this is a simple print statement in a Lambda function!")

    # You can return a response if needed
    return {
        'statusCode': 200,
        'body': 'Check CloudWatch logs for the printed message.'
    }