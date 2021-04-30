# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_result1"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Roll_Number=tracker.get_slot("roll_number"),
                                 choice=tracker.get_slot("semester"))

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_result2"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Roll_Number=tracker.get_slot("roll_number"),
                                 choice=tracker.get_slot("year"))

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_result3"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Roll_Number=tracker.get_slot("roll_number"),
                                 choice=tracker.get_slot("sub"))


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_result4"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_th",
                                 Roll_Number=tracker.get_slot("roll_number"))

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_show_map"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_show_map")


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_canteen_menu"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_canteen_menu")

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_tell_fee"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tell_fee")

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_campus_pictures"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_campus_pictures")                                                  

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_give_teacher_info"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_give_teacher_info")

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_give_hod_info"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_give_hod_info")