FROM public.ecr.aws/lambda/python:3.12

RUN yum update -y

COPY * ${LAMBDA_TASK_ROOT}/

RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt


