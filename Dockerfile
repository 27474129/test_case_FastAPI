FROM python:3.7.5

RUN mkdir /sources
COPY . /sources/
WORKDIR /sources


CMD cd /sources/
RUN pip3 install -r requirements.txt
CMD uvicorn app:app --reload
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
