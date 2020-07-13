from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction

import PyPDF2
import re
import json
from difflib import SequenceMatcher
import psycopg2 
import random
import uuid
from os import listdir, remove
from os.path import isfile, join, getmtime
import time

# TOCHANGE
# from database import Database
from .database import Database


class FindExerciseNos(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_exercise_nos"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        db = Database()
        exercises = db.get_exercises()

        buttons = []
        for exercise in exercises:
            exercise_no = str(exercise.exercise_no)
            payload = "/inform{\"exercise_no\": \"" + exercise_no + "\"}"
            buttons.append(
                {"title": "{}".format(exercise_no),
                 "payload": payload})


        dispatcher.utter_button_message("What exercise are you currently working on?", buttons)  
        return []   


class FindSubtaskNos(Action):
    """This action class retrieves the address of the user's
    healthcare facility choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_subtask_nos"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        exercise_no = tracker.get_slot("exercise_no")    

        db = Database()
        exercise_file = db.get_file_by_exercise_no(exercise_no)
        subtasks = db.get_subtasks_by_exercise_no(exercise_no)

        buttons = []
        for subtask in subtasks:
            subtask_no = str(subtask.subtask_no)
            payload = "/inform{\"subtask_no\": \"" + subtask_no + "\"}"
            buttons.append(
                {"title": "{}".format(subtask_no),
                "payload": payload})

        dispatcher.utter_message("Okay, you are working on exercise " + exercise_no + ".")
        dispatcher.utter_message(f'Here is the [exercise sheet]({exercise_file}).')
        dispatcher.utter_button_message("What subtask can I help you with?", buttons)  
        return []          


class SuggestCourseItems(Action):
    """This action class retrieves the address of the user's
    healthcare facility choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "suggest_course_items"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        found = False

        exercise_no = tracker.get_slot("exercise_no")  
        subtask_no = tracker.get_slot("subtask_no")  

        db = Database()
        course_items = db.get_course_items_by_subtask(exercise_no, subtask_no)

        max_items = 6
        k = max_items if len(course_items) > max_items else len(course_items)
        random_items = random.sample(course_items, k)

        buttons = []
        for item in random_items:
            found = True
            payload = "/ask_course_item{\"course_item\": \"" + item.title + "\"}"
            #payload = "/inform{\"subtask_no\": \"" + subtask_no + "\"}"
            buttons.append(
                {"title": "{}".format(item.title),
                "payload": payload})

        if found:
            dispatcher.utter_button_message("Can I help you with one of these topics? Otherwise you can also ask me a question directly!", buttons)  

        return [SlotSet("course_item_found", found)]  


class FindInPdf(Action):
    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_in_pdf"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        found = False
        course_item = tracker.get_slot("course_item")   

        if course_item:   
            # TOCHANGE
            # reader = PyPDF2.PdfFileReader("test.pdf")
            writer = PyPDF2.PdfFileWriter()

            filename = str(uuid.uuid4())
            
            slides_path = "/files/slides"
            files = [f for f in listdir(slides_path) if isfile(join(slides_path, f))]
            for file in files:
                reader = PyPDF2.PdfFileReader(open(f'{slides_path}/{file}','rb'))
                numPages = reader.getNumPages()
                for i in range(0, numPages):
                    pageObj = reader.getPage(i)
                    pdfText = pageObj.extractText()
                    resSearch = re.search(str(course_item).lower(), pdfText.lower())
                    if resSearch:
                        writer.addPage(pageObj)
                        path = f'/files/slide_extracts/{filename}.pdf'
                        with open(path, 'wb') as outfile:
                            writer.write(outfile)
                        found = True
            
            # delete old files
            slide_extracts_path = "/files/slide_extracts"
            files = [f for f in listdir(slide_extracts_path) if isfile(join(slide_extracts_path, f))]
            for file in files:
                last_change_time = getmtime(f'{slide_extracts_path}/{file}')
                if (time.time() - last_change_time) > 1800: # delete after 30 min
                    remove(f'{slide_extracts_path}/{file}')

            if found:
                dispatcher.utter_message(f'I picked out a few [slides](http://diarchitect-chatbot.de:8080/slide_extracts/{filename}.pdf) on the subject for you.')
                

        return [SlotSet("course_item_found", found),
                SlotSet("course_item", None)]


class FindInDb(Action):
    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_in_db"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        exercise_no = tracker.get_slot("exercise_no")    
        subtask_no = tracker.get_slot("subtask_no")    

        found = False
        course_item = tracker.get_slot("course_item")   

        if course_item:
            db = Database()
            course_items = db.get_course_items()

            for item in course_items:
                title = item.title
                similarity = SequenceMatcher(None, title.lower(), course_item.lower()).ratio()
                if similarity >= 0.8:
                    found = True
                    dispatcher.utter_message(item.description)
                    if item.how_to:
                        dispatcher.utter_message("Let me explain how to use it :)")
                        dispatcher.utter_message(item.how_to)
                    if item.file:
                        dispatcher.utter_message(image=item.file)    
                        if "diarchitect-chatbot" not in item.file:
                            dispatcher.utter_message(f'Image source: {item.file}')
                    if item.link:
                        dispatcher.utter_message(f'You can find further information [here]({item.link}) 🌐')  
                    if exercise_no and subtask_no:
                        how_to_exercise_specific = db.get_how_to_exercise_specific(course_item, exercise_no, subtask_no)   
                        if how_to_exercise_specific:
                            dispatcher.utter_message(f'Let me explain how you have to use {course_item} for exercise {exercise_no} subtask {subtask_no}.')
                            dispatcher.utter_message(how_to_exercise_specific) 
        
        return [SlotSet("course_item_found", found)]


class FillAdvancedHelpSlot(Action):
    def name(self) -> Text:
        """Unique identifier of the action"""

        return "fill_advanced_help_slot"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        exercise_no = tracker.get_slot("exercise_no")    
        subtask_no = tracker.get_slot("subtask_no")    

        advanced_help = False

        if str(exercise_no) in ["2"]:
            if str(subtask_no) in ["2"]:
                advanced_help = True

        return [SlotSet("advanced_help", advanced_help)]


class ResetCourseItemSlot(Action):
    def name(self) -> Text:
        """Unique identifier of the action"""

        return "reset_course_item_slot"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet("course_item", None)]