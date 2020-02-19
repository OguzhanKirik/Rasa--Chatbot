## bot challenge
* bot_challenge
  - utter_iamabot


## search profile happy path
* greet
  - utter_how_can_i_help
* search_profile
  - action_ask_profile
  - utter_did_that_help
* affirm
  - utter_anything_else
* deny
  - utter_goodbye


## search profile sad path
* greet
  - utter_how_can_i_help
* search_profile
  - action_ask_profile
  - utter_did_that_help
* deny
  - utter_how_can_i_help
* thanks
  - utter_goodbye


## birhtday_provider
* greet
  - utter_how_can_i_help
* birhtday_provider{"name": "Ryan Reyes"}
  - action_provide_birthdate
  - utter_anything_else
* deny
  - utter_goodbye

## address_provider
* greet
  - utter_how_can_i_help
* address_provider {"name":"Edward Henderson"}
  - action_provide_address
  - utter_did_that_help
* affirm
  - utter_anything_else
* deny
  - utter_goodbye


## mail_provider + address_provider
* greet
  - utter_how_can_i_help
* mail_provider{"name":"James Hernandez"}
  - action_provide_mail
  - utter_did_that_help
* affirm
  - utter_anything_else
* address_provider{"name":" Kim Kennedy"}
  - action_provide_address
  - utter_did_that_help
* affirm
  - utter_anything_else
* deny
  -utter_goodbye


## samegender_provider
* greet
  - utter_how_can_i_help
* samegender_provider{"gender":"male"}
  - action_provide_same_gender
  - utter_did_that_help
* affirm
  - utter_anything_else
* deny
  - utter_goodbye


## age_query + birthdate_provider positive
* greet
  - utter_how_can_i_help
* age_query{"gauge":"older", "age":"50"}
  - action_make_age_query
  - utter_anything_else
* birthdate_provider{"name": "Sydney Munoz"}
 - action_provide_birthdate
 - utter_did_that_help
* affirm
- utter_anything_else
* deny
- utter_goodbye

## age_query + birthdate_provider negative
* greet
  - utter_how_can_i_help
* age_query{"gauge":"older", "age":"50"}
  - action_make_age_query
  - utter_anything_else
* deny
- utter_goodbye


## opening hours of an exhition
  * greet
  - utter_how_can_i_help
  - opening_exhibition
  - form{"name":"opening_exhibition"}
  * opening_hours
  - utter_ask_day
  * day_specification{"date": "Saturday"}
  - utter_which_exhibition
  - form{"name": "null"}
  - utter_anything_else
* deny
  - utter_goodbye_