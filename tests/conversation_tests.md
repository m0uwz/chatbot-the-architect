#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## test_story_utter_e2s2_help_happy_path
* exercise_help: /exercise_help
    - find_exercise_nos   
* inform: [2](exercise_no)    
    - slot{"exercise_no":"2"}
    - find_subtask_nos
* inform: [2](subtask_no) 
    - slot{"subtask_no":"2"}
    - fill_advanced_help_slot
    - slot{"advanced_help": true}
    - utter_advanced_help    
* affirm: yes
    - utter_affirm_advanced_help
    - utter_e2s2_story_1
* affirm: yeah
    - utter_e2s2_story_2
    - utter_e2s2_story_3
* affirm: yep  
    - utter_e2s2_story_7
    - utter_e2s2_story_8
    - utter_e2s2_story_9
* affirm: sure
    - utter_e2s2_story_11
    - utter_e2s2_story_12
    - utter_e2s2_story_13
    - utter_e2s2_story_14
* affirm: yes    
    - utter_e2s2_story_15
    - utter_e2s2_story_16
    - utter_continue
* affirm: yes    
    - utter_e2s2_story_17
    - utter_e2s2_story_18
* affirm: sure    
    - utter_e2s2_story_20
    - utter_e2s2_story_21
* affirm: ok    
    - utter_e2s2_story_23
    - utter_e2s2_story_24
    - utter_e2s2_story_25
    - utter_e2s2_story_26
    - utter_e2s2_story_27
    - utter_continue
* affirm: yes    
    - utter_e2s2_story_28
    - utter_e2s2_story_29
    - utter_e2s2_story_30
    - utter_e2s2_story_31
    - utter_e2s2_story_32
    - utter_e2s2_story_33
    - utter_e2s2_story_34
* affirm: sure
    - utter_e2s2_story_40
    - utter_e2s2_story_41
    - utter_e2s2_story_42
    - utter_e2s2_story_43
    - utter_e2s2_story_44
* affirm: yep    
    - utter_e2s2_story_48
    - utter_e2s2_story_49
    - utter_end_conversation

## test_story_utter_e2s2_help_with_problems_and_questions_1
* exercise_help: /exercise_help
    - find_exercise_nos   
* inform: [2](exercise_no)     
    - slot{"exercise_no":"2"}
    - find_subtask_nos
* inform: [2](subtask_no) 
    - slot{"subtask_no":"2"}
    - fill_advanced_help_slot
    - slot{"advanced_help": true}
    - utter_advanced_help    
* affirm: yes
    - utter_affirm_advanced_help
    - utter_e2s2_story_1
* ask_course_item: what is an REST-based API?
    - find_in_db 
    - slot{"course_item_found": true} 
    - utter_e2s2_story_2
    - utter_e2s2_story_3
* ask_course_item: what is [Node.js](course_item)?
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - slot{"course_item_found": true} 
    - utter_continue
* affirm: yes    
    - utter_e2s2_story_3   
* deny: no    
    - utter_e2s2_story_4
    - utter_e2s2_story_5
* deny: nope    
    - utter_e2s2_story_6
* affirm: yes    
    - utter_e2s2_story_7
    - utter_e2s2_story_8
    - utter_e2s2_story_9
* deny: no
    - utter_e2s2_story_10
    - utter_send_contact_details
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_11
    - utter_e2s2_story_12
    - utter_e2s2_story_13
    - utter_e2s2_story_14
* deny: nope    
    - utter_e2s2_story_15
    - utter_e2s2_story_16
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_17
    - utter_e2s2_story_18
* deny: no    
    - utter_e2s2_story_19
    - utter_e2s2_story_20
    - utter_e2s2_story_21
* ask_course_item: please explain [Node.js](course_item) to me
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - slot{"course_item_found": true} 
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_21      
* deny: no    
    - utter_e2s2_story_22
    - utter_e2s2_story_23
    - utter_e2s2_story_24
    - utter_e2s2_story_25
    - utter_e2s2_story_26
    - utter_e2s2_story_27
    - utter_continue
* ask_course_item: I want to learn more about [Software architecture](course_item)
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue      
* affirm: yes   
    - utter_e2s2_story_28
    - utter_e2s2_story_29
    - utter_e2s2_story_30
    - utter_e2s2_story_31
    - utter_e2s2_story_32
    - utter_e2s2_story_33
    - utter_e2s2_story_34
* deny: nope
    - utter_e2s2_story_35
* affirm: yes
    - utter_e2s2_story_36    
* ask_course_item: I want information about the [Economic value](course_item)
    - find_in_db
    - slot{"course_item_found": true}  
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_37
* deny: no    
    - utter_e2s2_story_38
    - utter_send_contact_details
* ask_course_item: what is [System design](course_item)?
    - find_in_db
    - slot{"course_item_found": true}    
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_39
* affirm: yes    
    - utter_e2s2_story_40
    - utter_e2s2_story_41
    - utter_e2s2_story_42
    - utter_e2s2_story_43
    - utter_e2s2_story_44
* deny: no    
    - utter_e2s2_story_45
* deny: nope    
    - utter_e2s2_story_46
    - utter_e2s2_story_47
* affirm: yes    
    - utter_e2s2_story_48
    - utter_e2s2_story_49
    - utter_end_conversation   

## test_story_utter_e2s2_help_with_problems_and_questions_2
* exercise_help: /exercise_help
    - find_exercise_nos   
* inform: [2](exercise_no)     
    - slot{"exercise_no":"2"}
    - find_subtask_nos
* inform: [2](subtask_no) 
    - slot{"subtask_no":"2"}
    - fill_advanced_help_slot
    - slot{"advanced_help": true}
    - utter_advanced_help    
* affirm: yes
    - utter_affirm_advanced_help
    - utter_e2s2_story_1
* ask_course_item: what is an REST-based API?
    - find_in_db 
    - slot{"course_item_found": true} 
    - utter_e2s2_story_2
    - utter_e2s2_story_3
* ask_course_item: what is [Node.js](course_item)?
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - slot{"course_item_found": true} 
    - utter_continue
* ask_course_item: what is [Node.js](course_item)?
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - slot{"course_item_found": true} 
    - utter_continue    
* affirm: yes    
    - utter_e2s2_story_3   
* deny: no    
    - utter_e2s2_story_4
    - utter_e2s2_story_5    
* deny: nope    
    - utter_e2s2_story_6
* affirm: yes    
    - utter_e2s2_story_7
    - utter_e2s2_story_8
    - utter_e2s2_story_9
* deny: no
    - utter_e2s2_story_10
    - utter_send_contact_details
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_11
    - utter_e2s2_story_12
    - utter_e2s2_story_13
    - utter_e2s2_story_14
* deny: nope    
    - utter_e2s2_story_15
    - utter_e2s2_story_16
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_17
    - utter_e2s2_story_18
* deny: no    
    - utter_e2s2_story_19
    - utter_e2s2_story_20
    - utter_e2s2_story_21
* ask_course_item: please explain [Node.js](course_item) to me
    - find_in_db
    - slot{"course_item_found": false}
    - find_in_pdf
    - slot{"course_item_found": true} 
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_21      
* deny: no    
    - utter_e2s2_story_22
    - utter_e2s2_story_23
    - utter_e2s2_story_24
    - utter_e2s2_story_25
    - utter_e2s2_story_26
    - utter_e2s2_story_27
    - utter_continue
* ask_course_item: I want to learn more about [Software architecture](course_item)
    - find_in_db
    - slot{"course_item_found": true}
    - utter_continue      
* affirm: yes   
    - utter_e2s2_story_28
    - utter_e2s2_story_29
    - utter_e2s2_story_30
    - utter_e2s2_story_31
    - utter_e2s2_story_32
    - utter_e2s2_story_33
    - utter_e2s2_story_34
* deny: nope
    - utter_e2s2_story_35
* affirm: yes
    - utter_e2s2_story_36    
* ask_course_item: I want information about the [Economic value](course_item)
    - find_in_db
    - slot{"course_item_found": true}  
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_37
* deny: no    
    - utter_e2s2_story_38
    - utter_send_contact_details
* ask_course_item: what is [System design](course_item)?
    - find_in_db
    - slot{"course_item_found": true}    
    - utter_continue
* affirm: yes   
    - utter_e2s2_story_39
* affirm: yes    
    - utter_e2s2_story_40
    - utter_e2s2_story_41
    - utter_e2s2_story_42
    - utter_e2s2_story_43
    - utter_e2s2_story_44
* deny: no    
    - utter_e2s2_story_45
* deny: nope    
    - utter_e2s2_story_46
    - utter_e2s2_story_47
* affirm: yes    
    - utter_e2s2_story_48
    - utter_e2s2_story_49
    - utter_end_conversation       



## happy path 2
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy
* goodbye: bye-bye!
  - utter_goodbye

## sad path 1
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* affirm: yes
  - utter_happy

## sad path 2
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* deny: not really
  - utter_goodbye

## sad path 3
* greet: hi
  - utter_greet
* mood_unhappy: very terrible
  - utter_cheer_up
  - utter_did_that_help
* deny: no
  - utter_goodbye

## say goodbye
* goodbye: bye-bye!
  - utter_goodbye

## bot challenge
* bot_challenge: are you a bot?
  - utter_iamabot
