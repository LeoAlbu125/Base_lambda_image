FROM public.ecr.aws/lambda/python:3.12

COPY functions/Lambda_default/main.py ${LAMBDA_TASK_ROOT}/function_default/
COPY functions/Lambda_a/main.py ${LAMBDA_TASK_ROOT}/function_a/
COPY functions/Lambda_b/main.py ${LAMBDA_TASK_ROOT}/function_b/
COPY requirements.txt ${LAMBDA_TASK_ROOT}/

RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

CMD ["function_default.main.lambda_handler"]
