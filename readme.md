# TodoList

#### The cross-platform todo app is written in Python3 and use sqlite3 as database. Available for Windows, Linux and MacOS

### ScreenShot:

![](https://github.com/prozip/TodoList-serverless_app/raw/master/image/win_test.png)

| Linux                                                        | Mac OS                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://github.com/prozip/TodoList-serverless_app/raw/master/image/linux_test.png) | ![](https://github.com/prozip/TodoList-serverless_app/raw/master/image/macosx_test.png) |



### Features:

- Python as BackEnd, Html/CSS/JS as FrontEnd

- Small build size:  7.8MB (Windows version)

- Available on any system (even without modern webview runtime - Ex: Win7 support)

  

### Download:

- Windows version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/windows/todo.exe) (If no webview found  [≤ win7], then mshtml is used)

- Windows chromium embed version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/windows/todo_chromium.exe) (Just for testing, Not recommended)

- Linux version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/linux/todo) (WebKit rendering)

- MacOS version [here](https://github.com/prozip/TodoList-serverless_app/raw/master/build/macosx/todo) (WebKit rendering)

  

### Run from source code:

1. Setup [Git](https://git-scm.com/), Python 3 [≤3.7], [webview2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) runtime (if use), [cefpython3](https://pypi.org/project/cefpython3/) module (if use)

2. Clone source: `git clone https://github.com/prozip/TodoList-serverless_app/`

3. Install requirements: `pip install -r requirements.txt`

4. Run with: `python src/start.py`

   

### How to build ?

 Check out [PyInstaller](https://www.pyinstaller.org/) or [py2app](https://py2app.readthedocs.io/en/latest/)





### Work flow:

![app_flow](https://github.com/prozip/TodoList-serverless_app/raw/master/image/app_flow.png)



