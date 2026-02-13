FROM python:3.12-slim 
EXPOSE 5000/tcp
EXPOSE 500/udp
WORKDIR /app 
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN echo "$(pip install -r requirements.txt)"
RUN echo "$(python app.py | echo)"
