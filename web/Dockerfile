FROM python
WORKDIR /usr/src/app
copy requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
copy . .
CMD ["python","app.py"]
