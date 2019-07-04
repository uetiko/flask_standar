from abc import abstractmethod


class HelperProyect(object):
    @abstractmethod
    def proyect_name():
        return __name__


def create_project(flask, ConfigObject):
    """
    Args:
        flask (:obj:`flask.Flask`)
        ConfigObject
    """
    flask.config.from_object(ConfigObject)
    return flask


def main(proyect_service, db_service):
    return proyect_service, db_service
