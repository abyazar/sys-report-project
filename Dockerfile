FROM python:3.10-slim

WORKDIR /app

COPY report.py .
COPY run.sh .

RUN chmod +x run.sh

CMD ["/bin/bash", "./run.sh"]