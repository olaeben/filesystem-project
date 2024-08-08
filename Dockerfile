FROM python

WORKDIR /usr/src/app

COPY fileSystem.py .

CMD ["python3", "fileSystem.py"]