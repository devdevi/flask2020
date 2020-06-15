FROM python:3.6.5-slim


WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt  \
    pip install --upgrade pip

EXPOSE 80
CMD ["python3", "app.py"]
# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static

# COPY ./requirements.txt /var/www/requirements.txt
# RUN pip install -r /var/www/requirements.txt
