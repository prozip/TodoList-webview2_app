from db import myDB
import time

def fetchInit(window):
    # window.evaluate_js("exportData()")
    myDB.initFetch(window)


def run(window):
    print('backend running')
    fetchInit(window)
