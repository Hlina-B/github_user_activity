import argparse

def get_user_input():
    parser = argparse.ArgumentParser(description="Github User Activity")
    parser.add_argument("username", type=str, help="Enter your github username")
    return parser.parse_args()