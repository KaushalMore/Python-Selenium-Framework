import pytest

from utils.logger import get_logger


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        # self.logger = get_logger(self.__class__.__name__)
        self.logger = get_logger(self.__class__.__name__, request)
        self.logger.info(
            f"---------------- Test Started {self.__class__.__name__}-{request.node.name} ----------------")
        yield
        self.logger.info(
            f"----------------------------- Test Finished -----------------------------")
