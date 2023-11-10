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

### Method 1: Using pip

#### Step 3: Install required packages
Execute the following command:
```
pip install -r requirements.txt
```

#### Step 4: Run your device
Execute the following command:
```
on android studio run your emulator android, or connect your android device to computer
```

#### Step 5: Run the bot
Execute the following command:
```
pytest tests
```

---

### Method 2: Using poetry

#### Step 3: Install the project and dependencies
Execute the following command:
```
poetry install
```

#### Step 4: Run your device
Execute the following command:
```
on android studio run your emulator android, or connect your android device to computer
```

#### Step 5: Run the bot
Execute the following command:
```
poetry run pytest tests
```
