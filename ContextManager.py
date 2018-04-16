import contextlib
import time
import datetime
import traceback


class ExecutionInfo:
    """This is a context manager that prints the information (starting time of the execution, time elapsed on the
    execution, information on an exception raised in the code (if such occured)) on some code wrapped in this manager in
    some given file. For example:

    >>>with ExecutionInfo('somefile.txt'):
    >>>     pass

    Will print all the information in the file somefile.txt.
    """
    def __init__(self, path):
        """Constructor of class ExecutionInfo. Takes one parameter: path to the file.

        :param path: Path to the file you want to print the information in.
        :type path: str.
        """
        self.file_path = path

    def __enter__(self):
        """Method called on the entering of the code, wrapped by this context manager. Here we initialize starting time
        of the execution of the code."""
        self.time_start = time.time()
        self.execution_datetime = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Method called on the exiting of the code, wrapped by this context manager. Here we calculate time elapsed on
        the execution, open the output file, print all the required information and close the file.

        :param exc_type: Type of the exception raised in the wrapped code.
        :type exc_type: Exception.
        :param exc_val: Information on the exception raised in the wrapped code.
        :type exc_val: str.
        :param exc_tb: Traceback of the exception raised in the wrapped code.
        :type exc_tb: traceback.
        :return None.
        """
        self.time_elapsed = time.time() - self.time_start
        self.file = open(self.file_path, 'w')
        print('Information on the code executed on {}:\nTime elapsed on the execution of the code: {}'
              .format(self.execution_datetime, self.time_elapsed),
              file=self.file)
        if exc_type is None:
            print('No exceptions raised during the execution of the code.', file=self.file)
        else:
            print('Exception raised!\nTraceback (most recent call last):', file=self.file)
            traceback.print_tb(exc_tb, file=self.file)
            print('{}: {}'.format(exc_type.__name__, exc_val), file=self.file)
        self.file.close()


with ExecutionInfo('feedback.txt'):
    a = 1
    for i in range(1000000):
        a += 1
    print(a)
    print('aasdad' / 102103)
