# dockerKill
How to kill a docker container gracefully

## Introduction
This is sample project for creating docker process and pass interrupts signal to main process inside docker.
Advantages for these are we can gracefully kill process and save their state if required and remove unwanted files and connections.


## Running

```
docker build dockerKill .
docker run dockerKill
```

These commands will create and run the docker instances.

## Gracefully Kill the container

```
docker kill --signal="SIGTERM" <dockerId>
```

This command send SIGTERM signal to docker container.

```
def signal_handler(signal, frame):
    """Signal handler for the interrupt
    
    Arguments:
        signal {int} -- Signal id, eg 15 SIGTERM
        frame {object} -- Frame object for interrupt
    """

    for i in range(5, 0, -1):
        ##* Printing time to exist
        logging.error("Process will be terminated in {0}".format(i))
        time.sleep(1)
    sys.exit()
signal.signal(signal.SIGTERM, signal_handler)
```

This python code register signal_handler to `SIGTERM` interrupt signal and execute the interrupt handler (signal_handler)


## Sample Output

```
$ docker run dockerKill
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
WARNING:root:Running infinite Loop
ERROR:root:Process will be terminated in 5
ERROR:root:Process will be terminated in 4
ERROR:root:Process will be terminated in 3
ERROR:root:Process will be terminated in 2
ERROR:root:Process will be terminated in 1
$ 
```
