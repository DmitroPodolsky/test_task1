# Test Task 2

## Overview

This application is auto-test that login in app Ajax Security System and check that.

## Note

Make sure that you have add to your PATH ADB,ANDROID_HOME,ANDROID_SDK_ROOT and JAVA_HOME

## Prerequisites

- **Required**: Python 3.x
- **For pip method**: pip
- **For poetry method**: poetry

## Installation & Usage

---

#### Step 1: Clone the repository
Execute the following command:
```
git clone https://github.com/DmitroPodolsky/test_task1.git
```

#### Step 2: Navigate to the project directory
Execute the following command:
```
cd test_task1
```

#### Step 3: Set enviroment variables
Execute the following command:
```
Create a new .env file and transfer the keys from the existing .env.example file. 
```

### Method 1: Using pip

#### Step 4: Install required packages
Execute the following command:
```
pip install -r requirements.txt
```

#### Step 5: Run your device
Execute the following command:
```
on android studio run your emulator android, or connect your android device to computer
```

#### Step 6: Download the Ajax Security System app
you can it download from play market or from site https://apkpure.com/ajax-security-system/com.ajaxsystems/download?utm_content=1008 apk file, after that use command:
```
adb install your_path_to_apk_file
```

#### Step 7: Run the tests
Execute the following command:
```
pytest tests
```

---

### Method 2: Using poetry

#### Step 4: Install the project and dependencies
Execute the following command:
```
poetry install
```

#### Step 5: Run your device
Execute the following command:
```
on android studio run your emulator android, or connect your android device to computer
```

#### Step 6: Download the Ajax Security System app
you can it download from play market or from site https://apkpure.com/ajax-security-system/com.ajaxsystems/download?utm_content=1008 apk file, after that use command:
```
adb install your_path_to_apk_file
```

#### Step 7: Run the tests
Execute the following command:
```
poetry run pytest tests
```
