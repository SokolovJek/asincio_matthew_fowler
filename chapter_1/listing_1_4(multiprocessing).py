import multiprocessing
import os


def hello_from_process():
    print(f'привет от дочернего  процесса {os.getgid()}')

if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f'Привет от родительского процесса {os.getpid()}')
    hello_process.join()
