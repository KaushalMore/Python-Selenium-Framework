import pytest

from utils.logger import get_logger


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        # self.logger = get_logger(f"{self.__class__.__name__}.{request.node.name}")
        self.logger = get_logger(f"{self.__class__.__name__}.{request.node.name}", request)
        self.logger.info(f"----------------------------- Test Started ------------------------------")
        yield
        self.logger.info(f"----------------------------- Test Finished -----------------------------")
