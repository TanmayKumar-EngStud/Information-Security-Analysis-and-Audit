FROM python:3.7
WORKDIR /home/tanmay/Documents/Information Security Analysis and Audit/Telegram Bot with Database/Telegram Automator.py
COPY package*.json /home/tanmay/Documents/Information Security Analysis and Audit/
RUN pip install -r package*.json
ENV Port=8000
EXPOSE 8000
CMD ["python3", "Telegram Automator.py"]