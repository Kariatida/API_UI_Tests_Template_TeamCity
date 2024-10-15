import telebot
import os

from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'

from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'


bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
Human: {human_input}
Chatbot:"""

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=ChatOpenAI(max_tokens=1500,temperature=0.7,model_name='gpt-3.5-turbo'),
    prompt=prompt,
    memory=memory,
    verbose=True,
)
bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
print('start1')
def send_to_gtp(message_text):
    answer = llm_chain.predict(human_input=message_text)
    return answer

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот на базе gpt")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = send_to_gtp(message.text)
    bot.reply_to(message, response)
print('start2')
# Поллинг обновлений с использованием getUpdates
bot.polling()

import telebot
import os

from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEscan implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}import os

from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEscan implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
print('start1')
def send_to_gtp(message_text):
    answer = llm_chain.predict(human_input=message_text)
    return answer

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот на базе gpt")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = send_to_gtp(message.text)
    bot.reply_to(message, response)
print('start2')
# Поллинг обновлений с использованием getUpdates
bot.polling()

import telebot
import os'

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=ChatOpenAI(max_tokens=1500,temperature=0.7,model_name='gpt-3.5-turbo'),
    prompt=prompt,
    memory=memory,
    verbose=True,
)

print('start1')

import telebot
import os

from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
Human: {human_input}
Chatbot:"""

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
Human: {human_input}
Chatbot:"""


prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=ChatOpenAI(max_tokens=1500,temperature=0.7,model_name='gpt-3.5-turbo'),
    prompt=prompt,
    memory=memory,
    verbose=True,
)

print('start1')

from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
Human: {human_input}
Chatbot:"""
Answer in Russian

{chat_history}
print('start1')
def send_to_gtp(message_text):
    answer = llm_chain.predict(human_input=message_text)
    return answer

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот на базе gpt")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = send_to_gtp(message.text)
    bot.reply_to(message, response)
print('start2')
# Поллинг обновлений с использованием getUpdatesAnswer in Russian

{chat_history}
print('start1')
def send_to_gtp(message_text):
    answer = llm_chain.predict(human_input=message_text)
    return answer

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот на базе gpt")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = send_to_gtp(message.text)
    bot.reply_to(message, response)
print('start2')
# Поллинг обновлений с использованием getUpdates
prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=ChatOpenAI(max_tokens=1500,temperature=0.7,model_name='gpt-3.5-turbo'),
    prompt=prompt,
    memory=memory,
    verbose=True,
)
from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=ChatOpenAI(max_tokens=1500,temperature=0.7,model_name='gpt-3.5-turbo'),
    prompt=prompt,
    memory=memory,
    verbose=True,
)
from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'
tg_token = '6411150650:AAGp1_P9-alRuqh-U-V2neJ0h10SQXJ8eEs'

bot = telebot.TeleBot(tg_token)

template = """I want you to act as a mental health counselor. 
I need your guidance and advice on managing emotions, stress, anxiety and 
other mental health issues. You should use your knowledge of cognitive 
behavioral therapy, meditation techniques, mindfulness practices, 
and other therapeutic modalities to create strategies that a person 
can implement to improve their overall well-being.
First, try applying your knowledge of Stoicism.
Maximum response length 5 sentences
If possible, try to answer in 2-3 sentences.
You need to involve the user in a dialogue
Each sentence must be moved to a new line
Answer in Russian

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=ChatOpenAI(max_tokens=1500,temperature=0.7,model_name='gpt-3.5-turbo'),
    prompt=prompt,
    memory=memory,
    verbose=True,
)
