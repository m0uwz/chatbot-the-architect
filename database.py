from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_model import Exercise, Subtask, Lecture, CourseItem

class Database():
    def __init__(self):
        self.eng = create_engine("postgresql+psycopg2://postgres:admin@/chatbot")

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