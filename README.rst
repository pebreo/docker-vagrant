NOTE: None of these images seem to work. Waiting for Docker 1.0 to be released.
For now, I will still use Chef to provision my Vagrant boxes.


What is Docker?
--------------
Docker is software that makes it easier to manage linux containers which makes it
easier to provision linux environments.


Installation
-----------

How It Works on OS X
On a Mac you must install boot2docker. The way it works on a Mac is a Docker daemon runs in a Virtualbox virtual machine and you execute commands on the mac using the Docker client using the 'docker' command.

.. code:: bash

   $ brew update
   $ brew install boot2docker
   $ boot2docker init
   $ boot2docker up
   $ boot2docker ssh
   # pw: tcuser
   $ docker version # check the client

Edit your `.bash_profile`

.. code:: bash

   export DOCKER_HOST=tcp://localhost:4243
   alias d='docker'
   alias b2d='boot2docker'
   alias dl='docker ps -l -q' # get last container used


Running
-------

.. code:: bash

   # Run Docker commands without sudo
   $ sudo groupadd docker
   $ sudo gpasswd -a <msyusername> docker
   $ sudo service docker restart

   # start the Docker daemon
   $ b2d start 

   # build the image (from the Dockerfile) with tag
   $ d pull ubuntu
   $ d build -rm -t pebreo/myimage .

   # run the image 
   $ d run -d -p 8000:8000 -t pebreo/myimage

   # run interactive image
   $ d run -i -t pebreo/myimage /bin/bash

   # get the IP address
   $ sudo docker inspect <container_id> | grep IPAddress | cut -d '"' -f 4
 
   # kill docker image
   $ d ps -a
   $ d rm -f <containerid>
   # or
   $ d rm -f `dl` # dl is the last container id ran

   # delete docker image
   $ d rmi <container

   # push image to Docker index
   $ d login
   $ d push pebreo/myimage

References
---------

Vagrant provisioning via Docker - https://www.vagrantup.com/blog/feature-preview-vagrant-1-6-docker-dev-environments.html

Install Docker on a Mac -  http://docs.docker.io/installation/mac/

Bottle+Docker Hello World - https://github.com/joshuaconner/hello-world-docker-bottle
