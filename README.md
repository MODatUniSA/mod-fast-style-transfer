# MOD. image transfer server

A [TensorFlow convolutional neural network (CNN) for fast style transfer](https://github.com/lengstrom/fast-style-transfer) of an image’s style to another image.

## Setup

Clone this repository. Then run: (Warning: pulls down 13GB of pre-trained data)
```bash
# Build the docker image
$ docker build -t fast-style-transfer .

# List the docker image to check that it’s been built
$ docker images

# Run the image container
$ docker run -ti fast-style-transfer

# Setup the environment
$ source env/bin/activate

# Example style transfer
$ python evaluate.py --checkpoint path/to/style/model.ckpt \
  --in-path dir/of/test/imgs/ \
  --out-path dir/for/results/

# With the test image and scream model
$ python evaluate.py --checkpoint udlf_fst_checkpoints/scream.ckpt \
  --in-path in/ \
  --out-path out/
```

## TODO:

* ~~Get the Docker image running locally~~.
* ~~Generate some sample images~~.
* Train the network with our own source style.
* Setup a simple server to handle processing the image and sending it back.

Time so far: ~2 hours.

## License

Released under an [MIT License](LICENSE).

Copyright (c) 2017 [MOD.](https://mod.org.au)
Copyright (c) 2016 [Logan Engstrom](https://github.com/lengstrom/fast-style-transfer).
Thanks to [Thom Miano](https://github.com/thommiano) for the original Dockerfile.
