import subprocess
from typing import List
from typing import Optional

from appium.options.android import UiAutomator2Options
from loguru import logger


def get_connected_devices() -> Optional[List[str]]:
    """Returns a list of connected devices"""
    try:
        # Run the adb devices command to get the list of connected devices
        result = subprocess.run(
            ["adb", "devices"], capture_output=True, text=True, check=True
        )

        # Parse the output to extract the list of devices
        devices_output = result.stdout
        lines = devices_output.strip().split("\n")[1:]  # Skip the first line (header)
        devices = [
            line.split("\t")[0] for line in lines if line.strip()
        ]  # Extract udid from each line

        return devices
    except subprocess.CalledProcessError as error:
        logger.error(f"Error running 'adb devices': {error}")
        return []


def get_device_udid() -> Optional[str]:
    """Returns the udid of the first connected device"""
    devices = get_connected_devices()
    if devices:
        return devices[0]
    logger.warning("No connected devices found.")
    return None


def android_get_options_capabilities() -> UiAutomator2Options:
    """Returns the options and capabilities for the Android driver"""
    capabilities = dict(
        autoGrantPermissions=True,
        automationName="uiautomator2",
        newCommandTimeout=500,
        noSign=True,
        platformName="Android",
        platformVersion="9",
        resetKeyboard=True,
        systemPort=8301,
        takesScreenshot=True,
        appPackage="com.ajaxsystems",
        appActivity="com.ajaxsystems.ui.activity.LauncherActivity",
        udid=get_device_udid(),
    )

    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    logger.info("Capabilities loaded")
    return capabilities_options
