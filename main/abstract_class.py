from abc import ABC, abstractmethod


class JobSites(ABC):
    @abstractmethod
    def server_connection(self):
        pass

    @abstractmethod
    def job_dictionary(self, request):
        pass

    @abstractmethod
    def file_vacancy(self, jobs):
        pass