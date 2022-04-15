SHELL = /bin/bash
ESHOP_URL = http://10.6.0.93:5100
IMAGE_NAME = load_generator_selenium
CONTAINER_NAME = load_generator_selenium
NUM_USERS = 10

run:
	i=0; while [ $$i -lt ${NUM_USERS} ]; do \
		docker run --name $(CONTAINER_NAME)_$$i -d --network host -e ESHOP_URL=$(ESHOP_URL) --restart unless-stopped $(IMAGE_NAME); \
		i=`expr $$i + 1`; \
	done

build:
	docker build . -t $(IMAGE_NAME)

stop:
	i=0; while [ $$i -lt ${NUM_USERS} ]; do \
		docker kill $(CONTAINER_NAME)_$$i ; \
		docker rm $(CONTAINER_NAME)_$$i ; \
		i=`expr $$i + 1`; \
	done
