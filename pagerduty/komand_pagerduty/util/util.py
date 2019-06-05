
empty_user = {
    'id': '',
    'email': '',
    'name': '',
    'description': ''
}


def normalize_user(user):
    user['avatar_url'] = user.get('avatar_url') or ''
    user['color'] = user.get('color') or ''
    user['description'] = user.get('description') or ''
    user['email'] = user.get('email') or ''
    user['id'] = user.get('id') or ''
    user['name'] = user.get('name') or ''
    user['job_title'] = user.get('job_title') or ''
    user['role'] = user.get('role') or ''
    user['self'] = user.get('self') or ''
    user['summary'] = user.get('summary') or ''
    user['time_zone'] = user.get('time_zone') or ''
    return user
