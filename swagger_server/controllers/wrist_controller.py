import connexion
from swagger_server.models.location import Location
from swagger_server.models.state import State
from swagger_server.common.constants import AX12


def change_wrist(body):
    """
    Set wrist location

    :param body: Location object
    :type body: dict | bytes

    :rtype: Location
    """
    if connexion.request.is_json:
        body = Location.from_dict(connexion.request.get_json())

    location = body.location

    AX12.wrist(location)

    return Location(location)


def change_wrist_torque(body):
    """
    Set wrist torque

    :param body: Sate object
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = State.from_dict(connexion.request.get_json())

    state = body.state

    AX12.set_wrist_state(state)

    return State(state)


def read_wrist():
    """
    Get wrist location


    :rtype: Location
    """
    location = AX12.get_wrist()

    return Location(location)


def read_wrist_torque():
    """
    Get wrist torque


    :rtype: State
    """
    return State(True)
