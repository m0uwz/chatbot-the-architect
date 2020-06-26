from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# TOCHANGE
from database_model import Exercise, Subtask, Lecture, CourseItem
# from .database_model import Exercise, Subtask, Lecture, CourseItem

class Database():
    def __init__(self):
        # TOCHANGE
        self.eng = create_engine("postgresql+psycopg2://postgres:admin@/chatbot")
        # self.eng = create_engine("postgresql+psycopg2://admin:admin@chatbot-db/")

    def _open_session(self):
        DBSession = sessionmaker(bind=self.eng)
        session = DBSession()      
        return session      

    def get_exercises(self):
        session = self._open_session()
        exercises = session.query(Exercise)
        session.close()
        return exercises
    
    def get_subtasks_by_exercise_no(self, exercise_no):
        session = self._open_session()
        exercise = session.query(Exercise).filter(Exercise.exercise_no == exercise_no).first()
        subtasks = session.query(Subtask).filter(Subtask.exercise_id == exercise.id)
        session.close()
        return subtasks

    def get_lectures(self):
        session = self._open_session()
        subtasks = session.query(Lecture)
        session.close()
        return lectures

    def get_course_items(self):
        session = self._open_session()
        course_items = session.query(CourseItem)
        session.close()
        return course_items

    def get_course_items_by_subtask(self, exercise_no, subtask_no):
        session = self._open_session()
        exercise = session.query(Exercise).filter(Exercise.exercise_no == exercise_no).first()
        subtask = session.query(Subtask).filter(Subtask.exercise_id == exercise.id).filter(Subtask.subtask_no == subtask_no).first()
        course_item_relationships = subtask.course_items
        course_items = []
        for relationship in course_item_relationships:
            course_items.append(relationship.course_item)
        session.close()    
        return course_items