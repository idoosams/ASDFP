![build status](https://travis-ci.com/idoosams/ASDFP.svg?branch=master)
[![Documentation Status](https://readthedocs.org/projects/asdfp/badge/?version=latest)](https://asdfp.readthedocs.io/en/latest/?badge=latest)

# ASDFP - Advanced System Design Final Project

An example package. See [full documentation](https://asdfp.readthedocs.io/en/latest/?badge=latest).

## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:idoosams/ASDFP.git
    ...
    $ cd ASDFP/
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [ASD-Final Project] $ # you're good to go!
    ```

3. To check that everything is working as expected, run the tests:


    ```sh
    $ pytest tests/
    ...
    ```

## Deployment by docker

1. run from ASDFP:
    ```sh
    $ docker-compose build
    ...
    $ docker-compose up -d
    ```
2. you can generate configfiles with the config file generator (by defualt docker runs by configfile asd/config.ini).

3. 1. server (accept the sample) avaliable at port 5000
   2. Api\GUI(sorry about that :( ) at port 8000
   3. mq mannager is avaliable at the defult port 15672. (5672 avaliable as well)
   4. mongo db avaliable at the defult port 27017

4. data is presistent in asd/data (can be chaged into a virtual volume at the docker-compose file)
    
