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
    
# class ActionShowImage(Action):

#     def name(self) -> Text:
#         return "action_show_image"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(image="https://i.imgur.com/nGF1K8f.jpg")

#         return []


# - image: "https://media.istockphoto.com/id/1211384629/vector/psychologist-online-psychotherapy-practice-psychological-help-psychiatrist-consulting.jpg?s=170667a&w=0&k=20&c=K9rzaq43_jzfUIddP23AyLDHQwzBeYcoJXSfIjIZ7Hw="
#             title: "Image Description"
#             subtitle: "Click the image to visit the website"
#             buttons:
#               - title: "Visit Website"
#                 payload: "https://www.publico.pt/2021/10/10/p3/noticia/eis-dez-servicos-apoio-psicologico-acessiveis-pedir-ajuda-nao-pesadelo-1980389"
#     - text: "Meanwhile, can I help you with anything else right now?"


class ActionShowImageSupport(Action):
    def name(self) -> Text:
        return "action_show_image_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("<a href='https://www.publico.pt/2021/10/10/p3/noticia/eis-dez-servicos-apoio-psicologico-acessiveis-pedir-ajuda-nao-pesadelo-1980389'><img style='width: 15rem;' src='https://media.istockphoto.com/id/1211384629/vector/psychologist-online-psychotherapy-practice-psychological-help-psychiatrist-consulting.jpg?s=170667a&w=0&k=20&c=K9rzaq43_jzfUIddP23AyLDHQwzBeYcoJXSfIjIZ7Hw='></a>")
        # dispatcher.utter_message("Click <a href='https://www.publico.pt/2021/10/10/p3/noticia/eis-dez-servicos-apoio-psicologico-acessiveis-pedir-ajuda-nao-pesadelo-1980389'>here</a> to visit accessible support institutions")
        dispatcher.utter_message("Meanwhile, can I help you with anything else right now?")
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
            dispatcher.utter_message("Okay, I see you and I'm here to help you! I'll give you more information about that disease, so you'll be more informed!")
            dispatcher.utter_message("To help you understand if you are actually dealing with anxiety, here is a video that shows '7 Signs It Might Be Anxiety'. If you want, check it out")
            # <a href='https://www.youtube.com/watch?v=hm0_jrXqxR4'>here</a>
            dispatcher.utter_message('<iframe width="560" height="315" src="https://www.youtube.com/embed/hm0_jrXqxR4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
            dispatcher.utter_message("Otherwise, you can check this link with additional information about Anxiety: <a href='https://www.sns24.gov.pt/tema/saude-mental/ansiedade/#o-que-e-a-ansiedade'>click here</a>")
        elif "bipolar" in user_input:
            # Handle conversation differently for other conditions
            illness = "disease_bipolar"
            dispatcher.utter_message("Bipolar disease.")
        elif "depression" in user_input:
            illness = "disease_depression"
            dispatcher.utter_message("Okay, I see you and I'm here to help you! I'll give you more information about that disease, so you'll be more informed!")
            dispatcher.utter_message("To help you understand if you are actually dealing with depression, here is a video that shows '8 Types Of Depression You Should Know'. If you want, check it out")
            dispatcher.utter_message('<iframe width="560" height="315" src="https://www.youtube.com/embed/NDOeZD2F7jU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
            dispatcher.utter_message("Otherwise, you can check this link with additional information about Depression: <a href='https://www.sns24.gov.pt/tema/saude-mental/depressao/'>click here</a>")
        


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
            dispatcher.utter_message("Why not try coping strategies or relaxation techniques? Deep breathing exercises or mindfulness exercises can help. You could also try doing a physical activity you enjoy, such as walking, swimming or yoga. Don't forget to take time to look after yourself and do things that bring you joy and relaxation. For example, taking a warm bath, reading a book, practising mindfulness or meditation, or engaging in a hobby. Does this help?")

        return []
