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


def MultiFeelingsTemplate(feelings_list):
    res = ""
    for feelings in feelings_list:
        res += SingleFeelingsTemplate(feelings["value"],
                                      feelings["datetime"])
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


def MultiPoseTemplate(pose_list):
    res = ""
    for pose in pose_list:
        res += SinglePoseTemplate(pose["value"],
                                  pose["datetime"])
    return res


def SinglePoseTemplate(pose, datetime):
    return f"""
    <h4>Datetime - {datetime}</h4>
    <ul>
        <li>
            translation : x={pose['translation']['x']},
            y={pose['translation']['y']},
            z={pose['translation']['z']}
        </li>
        <li>rotation :
            x={pose['rotation']['x']},
            y={pose['rotation']['y']},
            z={pose['rotation']['z']},
            w={pose['rotation']['w']}
        </li>
    </ul>
    """
