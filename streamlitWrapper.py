import subprocess
import os

process = subprocess.Popen(["streamlit", "run", os.path.join(
            'C:/Users/zeeshan/Downloads/webcam-streaming-main/webcam-streaming-main/app.py')])

#OR

"""
process = subprocess.run(["streamlit", "run", os.path.join(
            'C:/Users/zeeshan/Downloads/webcam-streaming-main/webcam-streaming-main/app.py')])
"""



