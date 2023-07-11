import threading
from utility.logger import LoggerIfc

class JobScheduler:
    """
    Scheduler for running jobs in separate threads.

    Methods:
    - __init__(): Initialize a JobScheduler instance.
    - schedule(job, *args): Schedule a job to be executed.
    - run(): Run all scheduled jobs.

    Note: This class assumes the existence of threading and LoggerIfc libraries.
    """
    def __init__(self) -> None:
        """
        Initialize a JobScheduler instance.

        Parameters:
        None

        Returns:
        None

        This method initializes a JobScheduler instance. It sets up an empty list to store the scheduled jobs.

        Note: This method assumes the existence of the LoggerIfc class.
        """
        self.log = LoggerIfc("JobScheduler")
        self.__jobs = []

    def schedule(self, job, *args):
        """
        Schedule a job to be executed.

        Parameters:
        - job: The job function to be scheduled.
        - *args: Variable number of arguments to be passed to the job function.

        Returns:
        None

        This method schedules a job to be executed later. The job is passed as a function, and any additional arguments
        required by the job function can be provided.

        Note: This method assumes the existence of the threading library.
        """
        self.__jobs.append(threading.Thread(target=job, args=args))

    def run(self):
        """
        Run all scheduled jobs.

        Parameters:
        None

        Returns:
        None

        This method runs all the scheduled jobs in separate threads. It starts each thread, waits for all threads to
        complete, and then clears the list of scheduled jobs.

        Note: This method assumes the existence of the threading and LoggerIfc libraries.
        """
        self.log.debug("Running jobs")
        for job in self.__jobs:
            job.start()
        for job in self.__jobs:
            job.join()
        self.log.debug("All jobs completed")
        self.__jobs.clear()
        