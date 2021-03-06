Python Selenium runner is used to interact with the [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers) MVC app (running on port 5100).

# Build the image
`docker build . -t <image name>`
# Run the container
One container represents one user scenario executed until stopped. The scenario includes user registration, adding items to the cart, and ordering them.

`docker run --name <container name> -d --network host -e ESHOP_URL=<eshop domain name or IP> --restart unless-stopped <image name>`

Inspect the logs
```docker
docker logs -f <container name>
Setting up...
registration...
registered: u: waynerichardson@yahoo.com p: b(3rXhkA8s
logging in...
Ordering 8 items
Checkout..
Checkout succesful
returned back Home..
Scenario finished
logging in...
```
# Use Make
Edit Makefile by adding the image and container name, and eshop domain name or IP. You can also control the number of containers (users) using the `˙NUM_USERS` variable.
```shell
make build
make run
make stop
```