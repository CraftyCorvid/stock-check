FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get -y install cron

COPY . .

RUN printenv > /etc/environment
RUN (crontab -l ; echo "*/5 * * * * /usr/local/bin/python /usr/src/app/app.py > /proc/1/fd/1 2>/proc/1/fd/2") | crontab
CMD ["bash", "entrypoint.sh"]
# CMD ["python", "app.py"]