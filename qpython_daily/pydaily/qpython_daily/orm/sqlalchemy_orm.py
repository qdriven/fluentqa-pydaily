#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from qpython_daily.orm.sqlalchemy_demo import Base, meta_data, engine, session_factory

"""
Many-to-Many
"""


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    project_manager_id = Column(Integer, ForeignKey('project_manager.id'))
    ## relationship
    project_manager = relationship("ProjectManager", back_populates="projects")

    def __init__(self, title, description, project_manager, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.title = title
        self.description = description
        self.project_manager = project_manager


class ProjectManager(Base):
    __tablename__ = 'project_manager'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship("Project", back_populates="project_manager")

    def __init__(self, name, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.name = name


"""
one-to-one
"""


class Mobile(Base):
    __tablename__ = 'mobile'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    number = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, model, number, owner):
        self.model = model
        self.number = number
        self.owner = owner


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    mobile = relationship("Mobile", uselist=False, backref="owner")

    def __init__(self, name):
        self.name = name


def populate_database():
    session = session_factory()

    bruno = User("Bruno Krebs")
    john = User("John Doe")

    brunos_mobile = Mobile("android", "99991111", bruno)
    johns_mobile = Mobile("iphone", "55554444", john)

    session.add(brunos_mobile)
    session.add(johns_mobile)

    session.commit()
    session.close()


def query_users():
    session = session_factory()
    users_query = session.query(User)
    session.close()
    return users_query.all()


def query_mobiles():
    session = session_factory()
    mobiles_query = session.query(Mobile)
    session.close()
    return mobiles_query.all()


def populate_pm_database():
    session = session_factory()

    bruno = ProjectManager("Bruno Krebs")
    john = ProjectManager("John Doe")

    todo = Project("To-Do List", "Let's help people accomplish their tasks", bruno)
    moneyfy = Project("Moneyfy", "Best app to manage personal finances", john)
    questionmark = Project("QuestionMark", "App that simulates technical exams", bruno)
    blog = Project("NewBlog", "New blog engine that solves all issues", john)

    session.add(todo)
    session.add(moneyfy)
    session.add(questionmark)
    session.add(blog)

    session.commit()
    session.close()


def query_projects():
    session = session_factory()
    projects_query = session.query(Project)
    session.close()
    return projects_query.all()


association_table = Table(
    'association', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    students = relationship("Student", secondary=association_table)

    def __init__(self, title, description, students):
        self.title = title
        self.description = description
        self.students = students


def populate_st_database():
    session = session_factory()

    bruno = Student("Bruno Krebs")
    john = Student("John Doe")
    serena = Student("Serena Williams")
    jennifer = Student("Jennifer Garner")

    tenis = Course("Tenis Introduction", "Learn the basic rules of tenis", [bruno, john])
    chess = Course("Advanced Chess", "Learn advanced strategies", [serena])
    python = Course("Python Development", "Learn the basic concepts of Python", [serena, jennifer, john])

    session.add(tenis)
    session.add(chess)
    session.add(python)

    session.commit()
    session.close()


def query_courses():
    session = session_factory()
    course_query = session.query(Course)
    session.close()
    return course_query.all()


if __name__ == "__main__":
    meta_data.create_all(engine)
    Base.metadata.create_all(engine)
    users = query_users()
    if len(users) == 0:
        populate_database()
    """
    one-to-one
    """
    users = query_users()
    for user in users:
        print(f'{user.name} has an {user.mobile.model} with number {user.mobile.number}')
    """
    one-to-many
    """
    projects = query_projects()
    if len(projects) == 0:
        populate_pm_database()

    projects = query_projects()
    for project in projects:
        print(f'"{project.title}" is managed by {project.project_manager.name}')

    """
    many-to-many
    """
    courses = query_courses()
    if len(courses) == 0:
        populate_st_database()

        courses = query_courses()
    for course in courses:
        print(f'"{course.title}" has the following students: ', end="")

        for student in course.students:
            print(f'{student.name}; ', end="")

        print('')
