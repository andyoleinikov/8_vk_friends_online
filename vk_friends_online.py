import vk
import getpass
import sys
import settings


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass.getpass(prompt='Password: ', stream=None)


def get_online_friends(login, password, current_version='5.74'):
    session = vk.AuthSession(
        app_id=settings.APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=current_version)
    ids_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=ids_online)
    return friends_online


def output_friends_to_console(friends_online):
    print('Your friends online:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    if not login:
        sys.exit('You should input login')
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit('Authorization error, check login and password')
    output_friends_to_console(friends_online)
