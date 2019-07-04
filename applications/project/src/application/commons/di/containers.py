from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from dependency_injector.providers import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from applications.project.config.settings import ConfigApplication
from applications.project import HelperProyect
from applications.project import create_project
from applications.project import main


class CoreIoC(DeclarativeContainer):
    flask = Singleton(Flask, HelperProyect.proyect_name())
    config = Singleton(ConfigApplication)


class ServicesApplication(DeclarativeContainer):
    proyect_services = Callable(
        create_project, flask=CoreIoC.flask(), ConfigObject=CoreIoC.config()
    )
    db_service = Singleton(SQLAlchemy, proyect_services())
    migration_service = Singleton(Migrate, proyect_services(), db_service())


class ApplicationIoC(DeclarativeContainer):
    main = Callable(
        main, ServicesApplication.proyect_services(),
        ServicesApplication.db_service()
    )
