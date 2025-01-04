# You may need to add your working directory to the Python path. To do so, uncomment the following lines of code

import logging

from besser.bot.core.bot import Bot
from besser.bot.core.session import Session

from besser.bot.nlp.llm.llm_openai_api import LLMOpenAI
from besser.bot.core.processors.user_adaptation_processor import UserAdaptationProcessor
from besser.bot.core.processors.language_detection_processor import LanguageDetectionProcessor
from besser.bot.core.intent.intent import Intent
from besser.bot.nlp.intent_classifier.intent_classifier_prediction import IntentClassifierPrediction
# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')

# Create the bot
bot = Bot('adapted_gpt')
# Load bot properties stored in a dedicated file
bot.load_properties('config.ini')


gpt = LLMOpenAI(
    bot=bot,
    name='gpt-4o-mini',
    parameters={},
    num_previous_messages=10,
    global_context="You adapt your responses based on a given user profile, such as their native language, interests, and other attributes provided.\
Your goal is to enhance the user's user experience by tailoring your responses to their profile. "
)
# Define the platform your chatbot will use
websocket_platform = bot.use_websocket_platform(use_ui=True)

# STATES

initial_state = bot.new_state('initial_state', initial=True)
hello_state = bot.new_state('hello_state')
question_state = bot.new_state('question_state')
# INTENTS

hello_intent = bot.new_intent('hello_intent', [
    'hello',
    'hi',
])


# STATES BODIES' DEFINITION + TRANSITIONS


initial_state.when_intent_matched_go_to(hello_intent, hello_state)
initial_state.when_no_intent_matched_go_to(hello_state)


def hello_body(session: Session):
    with open("user_model.json", "r") as file:
        user_model_string = file.read()
        gpt.add_user_context(session=session, context= f"This is the user's profile\n+ {user_model_string}", context_name = "user_profile")
    session.reply(gpt.chat(session=session))
    
    
hello_state.set_body(hello_body)
hello_state.when_no_intent_matched_go_to(question_state)


def question_body(session: Session):
    session.reply(gpt.chat(session=session))


question_state.set_body(question_body)
question_state.when_no_intent_matched_go_to(question_state)


# RUN APPLICATION

if __name__ == '__main__':
    bot.run()
