FROM amazonlinux:2
RUN yum update -y
RUN yum install -y python3 python3-pip python3-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["run.py"]