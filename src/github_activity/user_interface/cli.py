import argparse

def get_user_input():
    parase = argparse.ArgumentParser(description="Github User Activity")
    parase.add_argument("username", type=str, help="Enter your github username")
    return parase.parse_args()