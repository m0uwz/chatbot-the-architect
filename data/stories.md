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
* affirm
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
    - slot{"course_item_found": true}
    - utter_ask_helpfulness
* affirm
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
    - slot{"course_item_found": true}
    - utter_ask_helpfulness
* deny
    - find_in_pdf
    - slot{"course_item_found": true}
    - utter_ask_helpfulness
* deny
    - utter_rephrase_question
* ask_course_item
    - find_in_pdf
    - slot{"course_item_found": true}
    - utter_ask_helpfulness
* deny
    - utter_can_not_help
    - utter_send_contact_details
* thanks
    - utter_noworries            
* goodbye
    - utter_goodbye

## story_general_question_course_item_not_found
* general_question
    - utter_ask_question
* ask_course_item
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - slot{"course_item_found": false}
    - utter_can_not_help
    - utter_send_contact_details
* thanks
    - utter_noworries            
* goodbye
    - utter_goodbye

## story_exercise_help_with_suggestions
* exercise_help
    - find_exercise_nos   
* inform{"exercise_no":"1"}    
    - slot{"exercise_no":"1"}
    - find_subtask_nos
* inform{"subtask_no":"1"}
    - slot{"subtask_no":"1"}
    - fill_advanced_help_slot
    - slot{"advanced_help": false}
    - suggest_course_items
    - slot{"course_item_found": true}    
* ask_course_item{"course_item":"System design"}
    - find_in_db
    - slot{"course_item_found": true}
    - utter_ask_helpfulness
* affirm
    - utter_joy
    - utter_further_question
* deny
    - utter_no_help_needed
* goodbye
    - utter_goodbye

## story_utter_e2s2_help
* exercise_help
    - find_exercise_nos   
* inform{"exercise_no":"2"}    
    - slot{"exercise_no":"2"}
    - find_subtask_nos
* inform{"subtask_no":"2"}
    - slot{"subtask_no":"2"}
    - fill_advanced_help_slot
    - slot{"advanced_help": true}
    - utter_advanced_help    
* affirm
    - utter_affirm_advanced_help
    - utter_e2s2_story_1
* ask_course_item{"course_item":"REST-based API"}
    - find_in_db 
    - slot{"course_item_found": true} 
    - utter_e2s2_story_2
    - utter_e2s2_story_3
* deny    
    - utter_e2s2_story_4
    - utter_e2s2_story_5
* deny    
    - utter_e2s2_story_6
* affirm    
    - utter_e2s2_story_7
    - utter_e2s2_story_8
    - utter_e2s2_story_9
* deny
    - utter_e2s2_story_10
    - utter_send_contact_details
    - utter_continue
* affirm    
    - utter_e2s2_story_11
    - utter_e2s2_story_12
    - utter_e2s2_story_13
    - utter_e2s2_story_14
* deny    
    - utter_e2s2_story_15
    - utter_e2s2_story_16
    - utter_continue
* affirm    
    - utter_e2s2_story_17
    - utter_e2s2_story_18
* deny    
    - utter_e2s2_story_19
    - utter_e2s2_story_20
    - utter_e2s2_story_21
* deny    
    - utter_e2s2_story_22
    - utter_e2s2_story_23
    - utter_e2s2_story_24
    - utter_e2s2_story_25
    - utter_e2s2_story_26
    - utter_e2s2_story_27
    - utter_continue
* affirm    
    - utter_e2s2_story_28
    - utter_e2s2_story_29
    - utter_e2s2_story_30
    - utter_e2s2_story_31
    - utter_e2s2_story_32
    - utter_e2s2_story_33
    - utter_e2s2_story_34
* deny
    - utter_e2s2_story_35
* affirm
    - utter_e2s2_story_36    
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}  
    - utter_e2s2_story_37
* deny    
    - utter_e2s2_story_38
    - utter_send_contact_details
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}    
    - utter_e2s2_story_39
* affirm    
    - utter_e2s2_story_40
    - utter_e2s2_story_41
    - utter_e2s2_story_42
    - utter_e2s2_story_43
    - utter_e2s2_story_44
* deny    
    - utter_e2s2_story_45
* deny    
    - utter_e2s2_story_46
    - utter_e2s2_story_47
* affirm    
    - utter_e2s2_story_48
    - utter_e2s2_story_49

## story_exercise_help_without_suggestions
* exercise_help
    - find_exercise_nos   
* inform{"exercise_no":"1"}    
    - slot{"exercise_no":"1"}
    - find_subtask_nos
* inform{"subtask_no":"1"}
    - slot{"subtask_no":"1"}
    - fill_advanced_help_slot
    - slot{"advanced_help": false}
    - suggest_course_items
    - slot{"course_item_found": false}
    - utter_ask_question    
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_ask_helpfulness
* affirm
    - utter_joy
    - utter_further_question
* deny
    - utter_no_help_needed
* goodbye
    - utter_goodbye
