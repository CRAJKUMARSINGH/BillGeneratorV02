#!/usr/bin/env python3
"""
Script to run the Bill Generator Streamlit app
This script handles the proper path setup and runs the app from the correct directory
"""
import sys
import os
from pathlib import Path

# Add the src directory to Python path
src_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(src_dir))

# Change to src directory
os.chdir(src_dir)

# Now run the Streamlit app
if __name__ == "__main__":
    import subprocess
    subprocess.run(["streamlit", "run", "app.py"])
