## happy_path
* greet
    - find_facility_types
* inform{"facility_type": "xubh-q36u"}    
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": 4245}
    - find_healthcare_address
    - utter_address
* thanks
    - utter_noworries

## happy_path_multi_requests
* greet
    - find_facility_types
* inform{"facility_type": "xubh-q36u"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": "747604"}
    - find_healthcare_address
    - utter_address
* search_provider{"facility_type": "xubh-q36u"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": 4245}   
    - find_healthcare_address
    - utter_address

## happy_path2
* search_provider{"location": "Austin", "facility_type": "xubh-q36u"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": "450871"}
    - find_healthcare_address
    - utter_address
* thanks
    - utter_noworries

## story_goodbye
* goodbye
    - find_in_pdf
    - utter_goodbye

## story_thankyou
* thanks
    - utter_noworries   

## story_find_course_item
* ask_course_item
    - find_in_pdf

## New Story

* greet
    - find_facility_types
* inform{"facility_type":"xubh-q36u"}
    - slot{"facility_type":"xubh-q36u"}
    - facility_form
    - form{"name":"facility_form"}
    - slot{"facility_type":"xubh-q36u"}
    - slot{"facility_type":"xubh-q36u"}
    - slot{"requested_slot":"location"}
* inform{"location":"San Francisco"}
    - slot{"location":"San Francisco"}
    - facility_form
    - slot{"location":"San Francisco"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"facility_id":"050228"}
    - slot{"facility_id":"050228"}
    - find_healthcare_address
    - slot{"facility_address":"1001 Potrero Avenue, San Francisco, CA 94110"}
    - utter_address
    - utter_noworries
* goodbye
    - utter_goodbye

## story_initial
* get_started
    - utter_greet
    - utter_ask_help_type


## story_general_question_helpful
* general_question
    - utter_ask_question
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_ask_helpfulness
* helpful
    - utter_joy
    - utter_further_question
* deny
    - utter_no_help_needed
* goodbye
    - utter_goodbye

## story_general_question_course_item_not_found_in_db_but_pdf
* general_question
    - utter_ask_question
* ask_course_item
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - utter_ask_helpfulness
* helpful
    - utter_joy
    - utter_further_question
* deny
    - utter_no_help_needed
* goodbye
    - utter_goodbye

## story_general_question_not_helpful
* general_question
    - utter_ask_question
* ask_course_item
    - find_in_db
    - utter_ask_helpfulness
* not_helpful
    - find_in_pdf
    - utter_ask_helpfulness
* not_helpful
    - utter_rephrase_question
* ask_course_item
    - find_in_pdf
    - utter_ask_helpfulness
* not_helpful
    - utter_can_not_help
    - utter_send_contact_details
* thanks
    - utter_noworries            
* goodbye
    - utter_goodbye                           

## story_exercise_help
* exercise_help
    - find_exercise_nos   
* inform{"exercise_no":"1"}    
    - slot{"exercise_no":"1"}
    - find_subtask_nos
* inform{"subtask_no":"1"}
    - slot{"subtask_no":"1"}    
    - utter_ask_question
* ask_course_item     
