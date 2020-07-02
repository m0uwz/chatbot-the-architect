## story_greet
* greet
    - utter_greet
    - utter_ask_help_type

## story_goodbye
* goodbye
    - utter_goodbye

## story_thankyou
* thanks
    - utter_noworries

## story_initial
* get_started
    - utter_greet
    - utter_ask_help_type

## story_out_of_scope
* out_of_scope
    - utter_out_of_scope

## story_joke
* joke
    - utter_joke    

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

## story_utter_e2s2_help_happy_path
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
* affirm
    - utter_e2s2_story_2
    - utter_e2s2_story_3
* affirm  
    - utter_e2s2_story_7
    - utter_e2s2_story_8
    - utter_e2s2_story_9
* affirm
    - utter_e2s2_story_11
    - utter_e2s2_story_12
    - utter_e2s2_story_13
    - utter_e2s2_story_14
* affirm    
    - utter_e2s2_story_15
    - utter_e2s2_story_16
    - utter_continue
* affirm    
    - utter_e2s2_story_17
    - utter_e2s2_story_18
* affirm    
    - utter_e2s2_story_20
    - utter_e2s2_story_21
* affirm    
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
* affirm
    - utter_e2s2_story_40
    - utter_e2s2_story_41
    - utter_e2s2_story_42
    - utter_e2s2_story_43
    - utter_e2s2_story_44
* affirm    
    - utter_e2s2_story_48
    - utter_e2s2_story_49
    - utter_end_conversation

## story_utter_e2s2_help_with_problems
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
    - utter_end_conversation

## story_utter_e2s2_help_with_problems_and_questions_1
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
* ask_course_item
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - slot{"course_item_found": true} 
    - utter_continue
* affirm    
    - utter_e2s2_story_3
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_3           
* deny    
    - utter_e2s2_story_4
    - utter_e2s2_story_5
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_5    
* deny    
    - utter_e2s2_story_6
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_6
* affirm    
    - utter_e2s2_story_7
    - utter_e2s2_story_8
    - utter_e2s2_story_9
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
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
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_14
* deny    
    - utter_e2s2_story_15
    - utter_e2s2_story_16
    - utter_continue
* affirm    
    - utter_e2s2_story_17
    - utter_e2s2_story_18
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_18
* deny    
    - utter_e2s2_story_19
    - utter_e2s2_story_20
    - utter_e2s2_story_21
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm    
    - utter_e2s2_story_21
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_21      
* deny    
    - utter_e2s2_story_22
    - utter_e2s2_story_23
    - utter_e2s2_story_24
    - utter_e2s2_story_25
    - utter_e2s2_story_26
    - utter_e2s2_story_27
    - utter_continue
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue      
* affirm    
    - utter_e2s2_story_28
    - utter_e2s2_story_29
    - utter_e2s2_story_30
    - utter_e2s2_story_31
    - utter_e2s2_story_32
    - utter_e2s2_story_33
    - utter_e2s2_story_34
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_34
* deny
    - utter_e2s2_story_35
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_35
* affirm
    - utter_e2s2_story_36    
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}  
    - utter_continue
* affirm    
    - utter_e2s2_story_37
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_37
* deny    
    - utter_e2s2_story_38
    - utter_send_contact_details
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}    
    - utter_continue
* affirm    
    - utter_e2s2_story_39
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_39
* affirm    
    - utter_e2s2_story_40
    - utter_e2s2_story_41
    - utter_e2s2_story_42
    - utter_e2s2_story_43
    - utter_e2s2_story_44
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_44
* deny    
    - utter_e2s2_story_45
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_45
* deny    
    - utter_e2s2_story_46
    - utter_e2s2_story_47
* ask_course_item
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue
* affirm
    - utter_e2s2_story_47
* affirm    
    - utter_e2s2_story_48
    - utter_e2s2_story_49
    - utter_end_conversation

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

## story_utter_e2s2_help_with_problems_and_questions_2

* get_started
    - utter_greet
    - utter_ask_help_type
* exercise_help
    - find_exercise_nos
* inform{"exercise_no":"2"}
    - slot{"exercise_no":"2"}
    - slot{"exercise_no":"2"}
    - find_subtask_nos
* inform{"subtask_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - fill_advanced_help_slot
    - slot{"advanced_help":true}
    - utter_advanced_help
* affirm
    - utter_affirm_advanced_help
    - utter_e2s2_story_1
* ask_course_item{"course_item":"REST-based API"}
    - slot{"course_item":"REST-based API"}
    - slot{"course_item":"REST-based API"}
    - find_in_db
    - slot{"course_item_found":true}
    - utter_e2s2_story_2
    - utter_e2s2_story_3
* ask_course_item{"course_item":"Node.js"}
    - slot{"course_item":"Node.js"}
    - slot{"course_item":"Node.js"}
    - find_in_db
    - slot{"course_item_found":false}
    - find_in_pdf
    - slot{"course_item_found":true}
    - slot{"course_item":null}
    - utter_continue
* affirm
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"course_item":"REST-based API"}
    - slot{"course_item":"Node.js"}
    - utter_e2s2_story_3
* deny
    - utter_e2s2_story_4
    - utter_e2s2_story_5
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"course_item":"REST-based API"}
    - slot{"course_item":"Node.js"}
* affirm
    - utter_e2s2_story_7
    - utter_e2s2_story_8
    - utter_e2s2_story_9
* ask_course_item{"course_item":"Software architecture"}
    - slot{"course_item":"Software architecture"}
    - slot{"course_item":"Software architecture"}
    - find_in_db
    - slot{"course_item_found":true}
    - utter_continue
* affirm
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
* ask_course_item{"course_item":"Node.js"}
    - slot{"course_item":"Node.js"}
    - slot{"course_item":"Node.js"}
    - find_in_db
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"course_item":"REST-based API"}
    - slot{"course_item":"Node.js"}
    - slot{"course_item":"Software architecture"}
    - slot{"course_item":"Node.js"}
    - find_in_pdf
    - slot{"course_item_found":true}
    - slot{"course_item":null}
    - utter_continue
* affirm
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"course_item":"REST-based API"}
    - slot{"course_item":"Node.js"}
    - slot{"course_item":"Software architecture"}
    - slot{"course_item":"Node.js"}
    - utter_e2s2_story_14
* affirm
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"course_item":"REST-based API"}
    - slot{"course_item":"Node.js"}
    - slot{"course_item":"Software architecture"}
    - slot{"course_item":"Node.js"}
    - utter_e2s2_story_15
    - utter_e2s2_story_16
    - utter_continue
* affirm
    - utter_e2s2_story_17
    - utter_e2s2_story_18
* affirm
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
    - utter_end_conversation

## story_exercise_help_without_advanced_help_and_without_suggestions

* greet
    - utter_greet
    - utter_ask_help_type
* exercise_help
    - find_exercise_nos
* inform{"exercise_no":"2"}
    - slot{"exercise_no":"2"}
    - slot{"exercise_no":"2"}
    - find_subtask_nos
* inform{"subtask_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"subtask_no":"2"}
    - fill_advanced_help_slot
    - slot{"advanced_help":true}
    - utter_advanced_help
* deny
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - suggest_course_items
    - slot{"course_item_found":false}
    - utter_ask_question
* ask_course_item{"course_item":"Software architecture"}
    - slot{"course_item":"Software architecture"}
    - find_in_db
    - slot{"course_item_found":true}
    - utter_ask_helpfulness

## story_utter_e2s2_help_with_problems_and_questions_3

* greet
    - utter_greet
    - utter_ask_help_type
* exercise_help
    - find_exercise_nos
* inform{"exercise_no":"2"}
    - slot{"exercise_no":"2"}
    - slot{"exercise_no":"2"}
    - find_subtask_nos
* inform{"subtask_no":"2"}
    - slot{"subtask_no":"2"}
    - slot{"subtask_no":"2"}
    - fill_advanced_help_slot
    - slot{"advanced_help":true}
    - utter_advanced_help
* affirm
    - utter_affirm_advanced_help
    - utter_e2s2_story_1
* affirm
    - utter_e2s2_story_2
    - utter_e2s2_story_3
* deny
    - utter_e2s2_story_4
    - utter_e2s2_story_5
* affirm
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
* affirm
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
* affirm
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
* deny
    - utter_e2s2_story_35
* deny
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - utter_send_contact_details
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - utter_e2s2_story_36
* deny
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - utter_e2s2_story_40
    - utter_e2s2_story_41
    - utter_e2s2_story_42
    - utter_e2s2_story_43
    - utter_e2s2_story_44
* deny
    - utter_e2s2_story_45
* affirm
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - utter_e2s2_story_47
* deny
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - utter_e2s2_story_46
    - utter_e2s2_story_47
* deny
    - slot{"exercise_no":"2"}
    - slot{"subtask_no":"2"}
    - utter_out_of_scope
    - utter_send_contact_details
* thanks
    - utter_noworries
