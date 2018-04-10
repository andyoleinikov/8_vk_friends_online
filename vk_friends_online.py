import vk
import getpass
import sys
import settings


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass.getpass(prompt='Password: ', stream=None)


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=settings.APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    ids_online = ', '.join((map(str, api.friends.getOnline(v=5.74))))
    friends_online = api.users.get(user_ids=ids_online, v=5.74)
    return friends_online


def output_friends_to_console(friends_online):
    print('Your friends online:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    if not login:
        sys.exit('You should type login')
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError as e:
        sys.exit(e)
    output_friends_to_console(friends_online)
