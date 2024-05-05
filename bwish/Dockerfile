FROM python:3.11.4-slim-buster

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED True
# RUN addgroup --system app && adduser --system --group app
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . ./
# Make RUN commands use the new environment:
RUN echo "Pre-entrypoint stage" >> ~/.bashrc

# RUN mkdir $APP_HOME/static

EXPOSE 5005
CMD gunicorn --bind 0.0.0.0:5005 --workers 2 --threads 8 --timeout 0 --limit-request-line 0 bwish.wsgi:application & python3 manage.py run_send_email