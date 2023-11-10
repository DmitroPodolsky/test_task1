from typing import List, Optional
from appium.options.android import UiAutomator2Options
import subprocess
from  loguru import logger

def get_connected_devices() -> Optional[List[str]]:
    try:
        # Run the adb devices command to get the list of connected devices
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)

        # Parse the output to extract the list of devices
        devices_output = result.stdout
        lines = devices_output.strip().split('\n')[1:]  # Skip the first line (header)
        devices = [line.split('\t')[0] for line in lines if line.strip()]  # Extract udid from each line

        return devices
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running 'adb devices': {e}")
        return []

def get_device_udid() -> Optional[str]:
    devices = get_connected_devices()
    if devices:
        return devices[0]
    else:
        logger.warning("No connected devices found.")
        return None

def android_get_desired_capabilities() -> UiAutomator2Options:
    capabilities = dict(
        autoGrantPermissions= True,
        automationName= 'uiautomator2',
        newCommandTimeout= 500,
        noSign= True,
        platformName= 'Android',
        platformVersion= '9',
        resetKeyboard= True,
        systemPort= 8301,
        takesScreenshot= True,
        appPackage= 'com.ajaxsystems',
        appActivity= 'com.ajaxsystems.ui.activity.LauncherActivity',
        udid = get_device_udid()
    )
    
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    logger.info(f"Capabilities loaded")
    return capabilities_options





