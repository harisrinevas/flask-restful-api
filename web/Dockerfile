FROM python:3
WORKDIR /usr/src/app
copy requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
copy . .
ENV FLASK_APP=app.py
CMD ["flask","run","--host","0.0.0.0"]