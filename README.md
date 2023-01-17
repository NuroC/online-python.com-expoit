# online-python.com-expoit
An exploit to access servers on online-python.com

## Usage

1. Import all those files into a project onto https://www.online-python.com/
2. Run PRIMFILENAV.py, then a prompt should appear that looks like this:
```
PID   USER     TIME  COMMAND
    1 root      0:29 node server_8080.js
  575 repl      0:00 [python3]
  577 repl      0:00 [python3]
 1022 repl      0:00 [g++]
 1023 repl      0:00 [cc1plus]
 1282 repl      0:00 [javac]
 2799 repl      0:00 [sh]
 6286 repl      0:00 python3 main.py

** Process exited - Return Code: 0 **
```

3. type “?python3 jammer.py” and press enter

Magic! Servers have now been jammed.


## How does it work?
The script "jammer.py" performs the following actions: it copies the file "cop.py" to the directory "/tmp/lol.py" and subsequently executes it on the server. The script "cop.py" or "/tmp/lol.py" retrieves a list of all active process IDs and terminates all processes except for the process of the server itself and its own process, effectively disabling the server and preventing the execution of any other programs.
