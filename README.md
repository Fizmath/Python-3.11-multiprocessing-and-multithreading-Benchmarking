

# Python 3.11 multiprocessing and multithreading Benchmarking compared to Python 3.10

 
The included [multi-proc_thread.py](multi-proc_thread.py) file generates random float and int nested lists i.e matrices, then does some manipulations with list comprehensions, lambda and map functions. The iteration loop then  mutates  matrix dimensions adding more elements in every iteration to get things rather heavy.


Download this repo to your local machine then pull these two docker images :

```bash
docker pull python:3.11.0-bullseye

docker pull python:3.10.8-bullseye

```

Open a `CMD` in the folder where you put the [multi-proc_thread.py](multi-proc_thread.py) file and run this command 


```bash
docker run -it --rm --privileged -v $(pwd):/myapp python:3.10.8-bullseye bash
```

it immeditely falls into the docker shell , type ` ls myapp/` to make sure that you are on the right path :

```bash
root@xxxxxx:/# ls myapp/
README.md  multi-proc_thread.py 
root@xxxxxx:/#
```

To get a fair results close peripheral applications and do not mouse click while testing in both cases.

Paste ' python3 myapp/multi-proc_thread.py' to the shell to run the test. It takes about a minute to finish :

```bash
root@xxxxxx:/# python3 myapp/multi-proc_thread.py
Matrix size 10000 .... done!
Matrix size 40000 .... done!
.

['py3.10.8', 'NO_thread() -> 10.1622 s', 'Threads(5,) -> 50.6150 s', 'Processes(5,) -> 15.6486 s']
root@xxxxxx:/# 
```


copy/paste  the final output into a text file for later comparison.

Shut down the container by 'CTRL+D` then start the second container 


```bash
docker run -it --rm --privileged -v $(pwd):/myapp python:3.11.0-bullseye bash

```


then run the test again  ...

with `intel®Core  i7 11800 ` i got these results :



|Benchmark        | py3.10.8         |  py3.11.0        | 
| ------------- |-------------|:-------------:|
| NO_thread        | 10.16 s     | 8.97  s ->   12% faster     |
| Threads(5,)      | 50.61 s     | 45.14 s ->   11% faster     |
| Processes(5,)    | 15.64  s    | 14.61 s ->   7 % faster     |



The results are jittery any time you run the tests, anyway, Python 3.11 is faster . 


You might  modify or enhance [multi-proc_thread.py](multi-proc_thread.py) to create more robust Benchmarking. 






