import platform
import os
import sys

def generate_report():
    print("--- System Report ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Current Working Directory: {os.getcwd()}")
    print("------------------------")

if __name__ == "__main__":
    generate_report()