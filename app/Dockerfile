FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY . .

EXPOSE 8000

CMD uvicorn api.main:app --host 0.0.0.0 --root-path ${API_ROOT_PATH}