FROM python:3.11-slim
WORKDIR /workspace
COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt
COPY orchestrator/ /workspace/orchestrator/
COPY terraform/ /workspace/terraform/
EXPOSE 8080
CMD ["python", "orchestrator/app.py"]
