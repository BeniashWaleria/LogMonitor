FROM python:3.6.1-alpine
ADD logger.py /
CMD ["python", "logger.py"]
EXPOSE 5001
COPY logger.py /logger.py
