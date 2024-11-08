import os

def lambda_handler(event, context):
    cwd = os.path.dirname(__file__)
    file_path = os.path.join(cwd, "test.txt")

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:", content)
    except Exception as e:
        print("Error reading file:", e)
    # You can return a response if needed
    return {
        'work dir':cwd,
        'file path':file_path,
        'statusCode': 200,
        'body': 'Check CloudWatch logs for the printed message.'
    }
    
    
