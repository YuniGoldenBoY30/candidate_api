FROM docker.uclv.cu/python:3.9

# set work directory
WORKDIR /usr/src/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .

RUN python3 -m pip --disable-pip-version-check install -r requirements.txt --index-url https://nexus.uclv.edu.cu/repository/pypi/simple/ --trusted-host nexus.uclv.edu.cu


# copy project
COPY . .

CMD [ "fixtures/install.sh"]
