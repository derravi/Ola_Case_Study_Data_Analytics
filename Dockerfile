FROM python:3.13.7

RUN mkdir -p ola_driving_churn_prediction

WORKDIR /ola_driving_churn_prediction

COPY . /ola_driving_churn_prediction

RUN pip install -r requirements.txt

ENV PORT=8000

EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]