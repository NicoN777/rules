FROM python:3.6-slim
ENV SECRET /secret/api.properties
RUN mkdir /secret
COPY api.properties /secret
COPY . /api
WORKDIR /api
RUN pip install --trusted-host pypi.python.org -r requirements.txt
WORKDIR /api/rulesapi
EXPOSE 11011
CMD ["python", "api.py"]
