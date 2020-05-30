def UserTemplate(user):
    return f"""
  <h3>User #{user['user_id']}:</h3>
    <ul>
        <li>username : {user['username']}</li>
        <li>gender : {user['gender']}</li>
        <li>birthday : {user['birthday']}</li>
        <li>user id : {user['user_id']}</li>
    </ul>
    """


def MultiFeelingsTemplate(feelings):
    res = ""
    for singel_feelings in feelings:
        res += SingleFeelingsTemplate(singel_feelings["value"],
                                      singel_feelings["datetime"])
    return res


def SingleFeelingsTemplate(feelings, datetime):
    return f"""
    <h4>Datetime - {datetime}</h4>
    <ul>
        <li>hanger : {feelings['hunger']}</li>
        <li>thirst : {feelings['thirst']}</li>
        <li>exhaustion : {feelings['exhaustion']}</li>
        <li>happiness : {feelings['happiness']}</li>
    </ul>
    """


def PoseTemplate(user):
    return f"""
  <h3>User #{user['user_id']}:</h3>
    <ul>
        <li>username : {user['username']}</li>
        <li>gender : {user['gender']}</li>
        <li>birthday : {user['birthday']}</li>
        <li>user id : {user['user_id']}</li>
    </ul>
    """
