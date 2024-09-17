
# Summer school 2024

Hello students!

  

Prepare for an amazing automotive summer school packed with excitement and discovery.

From thrilling submarines to enable your skills, we will (**literally**) __IMMERSE__ ourselves in a world of learning that will pique your interest and fuel your passion.

Accept the challenges, let your imagination run wild, and let's make this a memorable summer school!

  
  

Let's work together and may the best team win!!!

  

Before that, following some tips and tricks.

## Watercraft

Well student, they are the challenges. The watercraft will be the subject of this Hackathon!

  

To successful pass the challenges, you have to know how to interoperate with the watercraft.

  

The watercraft has 3 sections:

- the lower layer: where is installed and two DC brushless motors.

- the upper layer, equipped with RaspberryPi 4 and a Camera (and other cumbersome electronics units)

- the intermediate layer to make the previous two layers waterproof

  

Well, we have some sensors, actuators and a small single-board computers! So, that's all?

Obviously, no! Somebody can say we have also a pool!

  

By the way, some remarks could be interested to perfect immerse you into the Hackathon or just to refresh your mind a few moments before the bell rings and you will conquer the last points to wind the Hackathon!

  

Two DC brushless motors to drive the submarine on the submarines left/right wings of the lower layer.

  

On the upper layer, a camera allows you to take a pictures and videos.

  

Finally, a [RaspberryPi](https://en.wikipedia.org/wiki/Raspberry_Pi)[4](https://en.wikipedia.org/wiki/Raspberry_Pi_4) is installed into the upper layer.

  

Shall we race to win the Hackathon?

  

Not be hurried!

  

Electronic and mechanical parts and components have to be managed in something way!

  

The invisible world of software is slowly open to you.

  
  

[RaspberryPi](https://en.wikipedia.org/wiki/Raspberry_Pi) can control the sensors and actuators in [Python](https://www.python.org/about/gettingstarted/).

  
  

Now, we have the basic ingredients to dive into the submarine fundamental concepts.

  

## Development environment

To start to race for the summer, you need to set up your development environment:

- [Python 3.11.2](https://www.python.org/downloads/release/python-3112/) is the programming language and interpret that we will use to drive the submarine.

- [Poetry](https://python-poetry.org/) resolves and installs the dependencies that you need to face up the Hackathon.

- An IDE, maybe [Visual Studio code](https://code.visualstudio.com/) or [PyCharm Community Edition](https://www.jetbrains.com/products/compare/?product=pycharm-ce&product=pycharm)

  

In addition, the [RaspberryPi](https://en.wikipedia.org/wiki/Raspberry_Pi) has also an own operating system: the [Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS).

  

[Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS) is a Debian-based operating system and for allowing you to control the sensors and engine, you also need a operating system level libraries.

  

To install them and poetry, just run this command:

```bash

sudo  apt  install  -y  python3-poetry  build-essential  libcap-dev  libatlas-base-dev  ffmpeg  libopenjp2-7  libcamera-dev  libkms++-dev  libfmt-dev  libdrm-dev  libjpeg-dev  libtiff5-dev  cmake  git  pkg-config  libtiff-dev  libpng-dev  libavcodec-dev  libavformat-dev  libswscale-dev  libv4l-dev  libxvidcore-dev  libx264-dev  libgtk-3-dev  gfortran  python3-dev  qt5-qmake  qtbase5-dev  qtbase5-dev-tools  qttools5-dev-tools  libhdf5-103

```

  

However, the camera on the [RaspberryPi](https://en.wikipedia.org/wiki/Raspberry_Pi) isn't as simple as you could think.

By running the follow command, you could copy the needed library to [Python 3.11.2](https://www.python.org/downloads/release/python-3112/) installation folder and the [RaspberryPi](https://en.wikipedia.org/wiki/Raspberry_Pi) can take pictures and videos.

  

```bash

sudo  cp  -r  /usr/lib/python3/dist-packages/libcamera  /usr/lib/python3.11

sudo  cp  -r  /usr/lib/python3/dist-packages/pykms  /usr/lib/python3.11

```

  

Well done! Now, we should set up the working development environment.

  

First of all, we need to activate the [python virtual environment](https://docs.python.org/3/library/venv.html):

```bash

mkdir  frank

cd  ./frank

python  -m  venv  frank_venv

source  frank_venv/bin/activate

```

and in a single shot, [Poetry](https://python-poetry.org/) resolves and installs all the needed libraries:

```bash

poetry  install

```

Unfortunately, [RaspberryPi](https://en.wikipedia.org/wiki/Raspberry_Pi) is a small single-board computer and some libraries are not still compatible.

So, if we run the python, it couldn't work correctly. No worried!

We have a solution, not to become a billionaire, to run correctly the code, solving also the future conflicts.

  

Merely, downgrade the numpy library

  

```bash

pip  uninstall  numpy

pip  install  numpy==1.24.2

```

  

Then, we can check if the development environment is activated by running the main.

  

```bash

python  ./main.py

```

  

## Base project

For introducing you to the submarine, we gave you a base project as a starting point to race for the Hackathon.

  

The structure of the base project is listed and described below:

- /config **NO MODIFY**

- configuration.yml **NO MODIFY**

- /frank_manager

- /sensors_actuators 

- /neural_network

- /utils

- main.py




Inside the main.py script, we wrote an example of to correctly manage the engines and the camera. In a nutshell, you can manage the engines using their class object written into the Engine class and de Camera by its own class.

  
  

## `Engine` Object

The `Engine` object is designed to manage the operations of two engines (left and right).

It allows to start and stop the engines with a specified power percentage.

```python

from sensors_actuators.engine import Engine

engine =  Engine() # Instantiate the class

```

  

To drive using left engine, you can use the *start_left* method and pass the power percentage in the range [-100, +100].

Example, use left engine with 30% of power.

```python

engine.start_left(30)

```

To drive using right engine, you can use the *start_right* method and pass the power percentage in the range [-100, +100].

Example, use right engine with 80% of power.

```python

engine.start_right(80)

```

  

When you reach your desired position, you can stop the left engine, by using the *stop_left* method.

```python

engine.stop_left()

```

When you reach your desired position, you can stop the right engine, by using the *stop_right* method.

```python

engine.stop_right()
```

*Remember that the engines are not calibrated, so giving the same percentage of power from 0 to 100 to the right and left engines does not guarantee that the watercraft will go straight.*



  

## `Camera` Object

  

The `Camera` object is designed to retrieve the taken picture.

It allows to elaborate the taken picture by camera.

  

```python

from sensors_actuators.camera import RecognizedObject

recognized_object =  RecognizedObject()

block = recognized_object.get_recognized_object()

```

  


## `Remote Control`


The code we will provide you for the Raspberry already has all the setup done, with the libraries installed and numpy properly downgraded. Additionally, there is a small web server that runs on the Raspberry only if the attribute `web_api_enable` in the `conf/configuration.yml` folder is set to **true**. In that case, with simple POST requests, you will be able to control the watercraft's motors as shown in the example provided:

Method: `POST`
Address: `192.168.1.X:8000/engine`
Body type: `JSON`
Body:
```
	{
	"duty_cicle_lx"  :  X,
	"duty_cicle_rx"  :  Y
	}
```

Where `X` and `Y` are values in `[0,100]`
##





And now? The Hackathon can start !!!

  

It is your turn!

  
  

May the best team win!!!