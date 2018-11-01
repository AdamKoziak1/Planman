FROM python:3

ADD hello_world.py /

CMD ["python","./hello_world.py"]