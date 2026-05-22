from github_activity.configs.bootstrap import bootstrap
from github_activity.user_interface.cli import get_user_input
from github_activity.services.activity import get_user_github_activity

def main():
    bts = bootstrap()
    args = get_user_input()
    get_user_github_activity(args.username, bts)

if __name__ == '__main__':
    main()