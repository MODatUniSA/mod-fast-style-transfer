# MOD. image transfer server

A [TensorFlow convolutional neural network (CNN) for fast style transfer](https://github.com/lengstrom/fast-style-transfer) of an image’s style to another image.

## Setup

Clone this repository. Then run (you may need to sudo docker...):
```bash
# Build the docker image
$ docker build -t fast-style-transfer .

# List the docker image to check that it’s been built
$ docker images

# Run the image container
$ docker run -ti fast-style-transfer

# Run the image in the background
$ docker run -d -p 5000:5000 fast-style-transfer

# To attach to that running process, run $ docker ps to get the name.
$ docker attach container_name

# To create a new shell into that container
$ docker exec -ti container_name bash

# Setup the environment (if you're using Cuda)
$ source env/bin/activate

# Example style transfer
$ python evaluate.py --checkpoint path/to/style/model.ckpt \
  --in-path dir/of/test/imgs/ \
  --out-path dir/for/results/

# With the test image and scream model
$ python evaluate.py --checkpoint udlf_fst_checkpoints/scream.ckpt \
  --in-path in/ \
  --out-path out/

# In a new terminal window (don’t exit from the Docker container), get the name of the running container
$ docker ps

# Then copy the output folder to your computer.
$ docker cp container_name:/root/fast-style-transfer/out .
```

## TODO:

* ~~Get the Docker image running locally~~.
* ~~Generate some sample images~~.
* Train the network with our own source style.
* ~~Setup a simple server to handle processing the image and sending it back.~~

Time so far: ~12 hours.

## License

Released under an [MIT License](LICENSE).

Copyright (c) 2017 [MOD.](https://mod.org.au)

Copyright (c) 2016 [Logan Engstrom](https://github.com/lengstrom/fast-style-transfer).

Thanks to [Thom Miano](https://github.com/thommiano) for the original Dockerfile.
