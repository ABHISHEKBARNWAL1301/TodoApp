FROM python:3
WORKDIR C:\Users\ASUS\Desktop\TODO-APP\backend\main
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "python", "main.py" ]