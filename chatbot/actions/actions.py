# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    
class ActionShowImage(Action):

    def name(self) -> Text:
        return "action_show_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://i.imgur.com/nGF1K8f.jpg")

        return []
    
class ActionDifferentiateConversation(Action):
    def name(self) -> Text:
        return "action_differentiate_illness"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message['text']
        
        # Perform differentiation logic based on the user input
        if "anxiety" in user_input:
            # Handle conversation differently for this condition
            illness = "disease_anxiety"
            dispatcher.utter_message("Anxiety is a normal reaction to danger or everyday stress. It is a feeling of fear or concern about a potential negative outcome. When anxiety becomes excessive and/or prolonged, extending beyond the triggering event, it can be classified as an anxiety disorder. This disorder is characterized by a severe and disproportionate fear that lasts for at least 6 months, significantly impacting the individual's daily life and functioning.")
            dispatcher.utter_message("Important symptoms of anxiety include excessive worry or fear, physical symptoms like rapid heartbeat and muscle tension, and sleep disturbances. Other signs include irrational thoughts, avoidance behaviors, difficulty concentrating, changes in appetite, irritability, social withdrawal, and physical discomfort.")
        elif "bipolar" in user_input:
            # Handle conversation differently for other conditions
            illness = "disease_bipolar"
            dispatcher.utter_message("Bipolar disease.")
        elif "depression" in user_input:
            illness = "disease_depression"
            dispatcher.utter_message("Depression.")


        return [SlotSet("illness", illness)]
    

class ActionSuggestionsByIllness(Action):
    def name(self) -> Text:
        return "action_suggest_by_illness"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[Dict[Text, Any]]:
        illness = tracker.get_slot("illness")

        if illness == "disease_anxiety":
            dispatcher.utter_message("Let's start then by trying to calm down and keep a cool head to deal with the situation. Take a deep breath and try grounding techniques like focusing on your senses or using relaxation exercises. It may also help to engage in activities you enjoy or find calming, such as listening to music or going for a walk. Does this make sense for you?")
        elif illness == "disease_bipolar":
            dispatcher.utter_message("SUGESTÕES DOENÇA BIPOLAR")
        elif illness == "disease_depression":
            dispatcher.utter_message("SUGESTÕES DEPRESSÃO")

        return []
