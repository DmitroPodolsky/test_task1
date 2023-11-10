import subprocess
import time

import pytest
from appium import webdriver
from loguru import logger

from utils.android_utils import android_get_desired_capabilities
from utils.config import settings


@pytest.fixture()
def run_appium_server():
    logger.info("setting up the server...")
    subprocess.Popen(
        ["appium", "-a", "0.0.0.0", "-p", "4723", "--allow-insecure", "adb_shell"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True,
    )
    logger.success("server is up and running")
    time.sleep(5)


@pytest.fixture()
def driver(run_appium_server):
    logger.info("setting up the driver...")
    driver = webdriver.Remote(
        settings.APPIUM_SERVER_URL, options=android_get_desired_capabilities()
    )
    logger.success("driver is ready")
    yield driver
