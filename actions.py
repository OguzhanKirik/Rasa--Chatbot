from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import mysql.connector
import database as db
import csv

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []




class ActionAskProfile(Action):
	def name(self) -> Text:
		return "action_ask_profile"
	def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
		name = tracker.latest_message['entities'][0]['value']
        
		query = db.database("mydatabase")
		result = query.data_searching(table_name= "profiles",fields = "name",data=name)

        	

        	#q = "select * from profiles where name='{0}' limit 1".format(name)        
        	#result = db.query(q)
		#print(type(result))    
		if len(result) == 0:
			dispatcher.utter_message("Name is not found in the profiles")
		else:
			dispatcher.utter_message("Here is the profile {}".format(result))
		#return [SlotSet("gender",result[2])]
        
class ActionProvideAddress(Action):
	def name(self) -> Text:
		return "action_provide_address"
	def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
		name = tracker.latest_message['entities'][0]['value']
        
		query = db.database("mydatabase")
		result = query.data_searching(table_name= "profiles",fields = "name",data=name)
		address = result[3]
        	#q = "select * from profiles where name='{0}' limit 1".format(name)        
        	#result = db.query(q) 
		if len(result) == 0:
			dispatcher.utter_message("Name is not found in the profiles")
		else:
			dispatcher.utter_message("The address of is {}".format(address))

class ActionProvideBirhtdate(Action):
	def name(self) -> Text:
		return "action_provide_birthdate"
	def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
		name = tracker.latest_message['entities'][0]['value']
        
		query = db.database("mydatabase")
		result = query.data_searching(table_name= "profiles",fields = "name",data=name)
		birthdate = result[5]
        	#q = "select * from profiles where name='{0}' limit 1".format(name)        
        	#result = db.query(q) 
		if len(result) == 0:
			dispatcher.utter_message("Name is not found in the profiles")
		else:
			dispatcher.utter_message("The birhtdate is {}".format(birthdate))

class ActionProvideMail(Action):
	def name(self) -> Text:
		return "action_provide_mail"
	def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
		name = tracker.latest_message['entities'][0]['value']
        
		query = db.database("mydatabase")
		result = query.data_searching(table_name= "profiles",fields = "name",data=name)
		mail = result[4]
        	#q = "select * from profiles where name='{0}' limit 1".format(name)        
        	#result = db.query(q) 
		if len(result) == 0:
			dispatcher.utter_message("Name is not found in the profiles")
		else:
			dispatcher.utter_message("The mail is {}".format(mail))

class ActionProvideSameGender(Action):
	def name(self) -> Text:
		return "action_provide_same_gender"
	def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ## extact the entity
		gender = tracker.latest_message['entities'][0]['value']
		if gender == "female":
			g = 'F'
		else:
			g = 'M'
        ##obtain every profile with its name and sex in the dataset 
		query = db.database("mydatabase")
		profiles = query.select_data(table_name= "profiles", fields = ["name", "sex"])
		result = []
		for i in range(len(profiles)):
			if profiles[i][1] == g:
				result.append(profiles[i][0])

        	#q = "select * from profiles where name='{0}' limit 1".format(name)        
        	#result = db.query(q) 
		if g == 'F':
			dispatcher.utter_message("Female artists are {}".format(result))
		else:
			dispatcher.utter_message("Male artists are {}".format(result))

class ActionMakeAgeQuery(Action):
	def name(self) -> Text:
		return "action_make_age_query"
	def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ## extact the entity
		gauge = tracker.latest_message['entities'][0]['value']
		age = tracker.latest_message['entities'][1]['value']
		age = int(age)
		
        ##obtain every profile with its name and sex in the dataset 
		query = db.database("mydatabase")
		profiles = query.select_data(table_name= "profiles", fields = ["name", "birthdate"])
		result = []

		for i in range(len(profiles)):
			date = profiles[i][1]
			year = int(date[0:4])
			real_age = 2020 - year
			
			if gauge == 'older':
				if real_age > age:
					result.append(profiles[i][0])
			else:
				if real_age <= age:
					result.append(profiles[i][0])	
        	#q = "select * from profiles where name='{0}' limit 1".format(name)        
        	#result = db.query(q) 
		if gauge =='older':
			dispatcher.utter_message("Older artists are {}".format(result))
		else:
			dispatcher.utter_message("Younger artists are {}".format(result))



#class ActionHelloWorld(Action):
#	def name(self) -> Text:
#         return "action_query_world"
#
#    def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#		dispatcher.utter_message("Hello World!")
#
#        return []





class OpeningExhibition(FormAction):
	"""Custom form action to fill all slots required to find specific type
	of healthcare facilities in a certain city or zip code."""
	def name(self) -> Text:
		"""Unique identifier of the form"""

		return "opening_exhibition"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""

		return ["date", "exhibition"]

	def slot_mappings(self) -> Dict[Text, Any]:
		return {"date": self.from_entity(entity="date",
										intent=["day_specification",
										"opening_hours"])}
"""
				"exhibition": self.from_entity(entity="mail",
										intent=["get_mail"])}
"""
	def submit(self,
				dispatcher: CollectingDispatcher,
				tracker: Tracker,
				domain: Dict[Text, Any]
				) -> List[Dict]:
		"""Once required slots are filled, print buttons for found facilities"""

		date = tracker.get_slot('date')
		exhibition = tracker.get_slot('exhibition')

		print(exhibition,date)

		'''
		'''button_name = _resolve_name(FACILITY_TYPES, facility_type)'''
		if len(results) == 0:
			dispatcher.utter_message(
				"Sorry, we could not find a {} in {}.".format(name)) 

		else:
			dispatcher.utter_message(
                "Desired information is sent to {} e-mail address".format(mail))
