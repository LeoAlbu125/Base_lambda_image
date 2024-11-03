def lambda_handler(event, context):
    print("Hello, this is a default function")

    # You can return a response if needed
    return {
        'statusCode': 200,
        'body': 'this is the default function.'
    }