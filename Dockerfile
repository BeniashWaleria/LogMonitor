FROM python:3.6.1-alpine
ADD logger.py /
RUN pip install docker
CMD ["python", "logger.py"]
COPY logger.py /logger.py
