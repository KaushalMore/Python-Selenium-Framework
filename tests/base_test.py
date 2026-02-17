import pytest

from utils.logger import get_logger


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info("----------------Test Started----------------")
        yield
        self.logger.info("----------------Test Finished---------------")
