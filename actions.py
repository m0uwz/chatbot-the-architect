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

# TOCHANGE
from database import Database
# from .database import Database


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
        subtasks = db.get_subtasks_by_exercise_no(exercise_no)

        buttons = []
        for subtask in subtasks:
            subtask_no = str(subtask.subtask_no)
            payload = "/inform{\"subtask_no\": \"" + subtask_no + "\"}"
            buttons.append(
                {"title": "{}".format(subtask_no),
                "payload": payload})

        dispatcher.utter_message("Okay, you are working on exercise " + exercise_no + ".")
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

        k = 3 if len(course_items) > 3 else len(course_items)
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

        exercise_no = tracker.get_slot("exercise_no")    
        subtask_no = tracker.get_slot("subtask_no")    


        found = False
        course_item = tracker.get_slot("course_item")   

        if course_item: 
            dispatcher.utter_message("I found this slot course item:")
            dispatcher.utter_message(str(course_item))

                    
            # TOCHANGE
            # reader = PyPDF2.PdfFileReader("/app/actions/test.pdf")
            reader = PyPDF2.PdfFileReader("test.pdf")
            # writer = PyPDF2.PdfFileWriter()
            
            numPages = reader.getNumPages()

            for i in range(0, numPages):
                PageObj = reader.getPage(i)
                # dispatcher.utter_message("this is page " + str(i)) 
                pdfText = PageObj.extractText()
                # print(Text)
                resSearch = re.search(str(course_item).lower(), pdfText.lower())
                if resSearch:
                    # writer.addPage(PageObj)
                    # with open('/app/actions/outputi.pdf', 'wb') as outfile:
                        # writer.write(outfile)
                    found = True
                    dispatcher.utter_message(pdfText)
            
            #dispatcher.utter_message("Der Aufruf klappt schon mal... :-)")     
            #dispatcher.utter_message(image="https://i.imgur.com/nGF1K8f.jpg")
            #dispatcher.utter_message(
            #        text=(
            #            f"I did not find any matching issues on our [forum](https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf):\n"
            #            f"I recommend you post your question there."
            #        )
            #    )

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
            dispatcher.utter_message("I found this slot course item:")
            dispatcher.utter_message(str(course_item))

            db = Database()
            course_items = db.get_course_items()

            for item in course_items:
                title = item.title
                similarity = SequenceMatcher(None, title.lower(), course_item.lower()).ratio()
                if similarity >= 0.8:
                    found = True
                    dispatcher.utter_message(item.description)

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
            print("ich bin 2 ex")
            if str(subtask_no) in ["2"]:
                print("ich bin 2 sub")
                advanced_help = True

        return [SlotSet("advanced_help", advanced_help)]