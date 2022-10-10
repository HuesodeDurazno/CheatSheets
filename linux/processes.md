### listar procesos
    ps
        x running processes
        ax Show all processes on the system, not just the  ones you own.
        u Include more detailed information on processes.
        w Show full command names, not just what fits on one line.

#### informacion sobre los procesos
1.PID -> process id
2.TTY -> terminal device where the process is running
3.STAT -> process status
4.TIME
5.COMMAND
### terminar procesos
    kill pid

    puedes añadir señales

    para frezzear un proceso:
    kill -STOP pid

    un proceso detenido esta aun en memoria puedes reanudarlo con 
    kill -CONT pid

    forma brutal 
    kill -KILL

    ver señales por numero
    kill -l

### mandar a background un processo
    gunzip file.gz &
