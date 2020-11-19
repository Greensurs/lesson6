FROM python

WORKDIR /src

COPY ./requirements.txt /spc/requirements.txt
RUN pip install -r requirements.txt

COPY ./ /spc/

ENV FLASK_APP program.py
CMD flask run -h 0.0.0.0