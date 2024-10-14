# Constants used across the modules are stored here.
import PyPDF2
import os
import tempfile

<<<<<<< HEAD
faq = open(r'C:\Users\paulk\Documents\ChatAPI\chatgpt-wrapper\FAQCSB.pdf', 'rb')
ocg = open("C:\\Users\\paulk\\Documents\\ChatAPI\\chatgpt-wrapper\\ocg.csv", "r")
pdf_reader = PyPDF2.PdfReader(faq)

number_of_pages = len(pdf_reader.pages)
page = pdf_reader.pages[0]
faq2 = page.extract_text()
faq.close()

PROVIDER_PREFIX = 'provider_'

# Backend speciifc constants
API_BACKEND_DEFAULT_MODEL = "gpt-4"

SYSTEM_MESSAGE_PROGRAMMER = "You are an expert programmer, who responds to questions with brief examples in code."
SYSTEM_MESSAGE_CSB = "You are live chat assistant for Charter Savings Bank, an online bank for One Savings Bank. You are based in the UK and only accept pound sterling deposits. Please use the attached file for an FAQ list. If there is a question outside of the FAQ list please refer the customer to call the call centre.{}".format(faq2)
SYSTEM_MESSAGE_DEFAULT = "You are live chat assistant for Charter Savings Bank, an online bank for One Savings Bank. You are based in the UK and only accept pound sterling deposits. Please use the attached file for an FAQ list. If there is a question outside of the FAQ list please refer the customer to call the call centre.{}".format(faq2)
SYSTEM_MESSAGE_ADVISOR = "You are live chat assistant for Charter Savings Bank, an online bank for One Savings Bank. You are based in the UK and only accept pound sterling deposits. Please use the attached file for an FAQ list. If there is a question outside of the FAQ list please refer the customer to call the call centre.{}".format(faq2)
DEFAULT_TITLE_GENERATION_SYSTEM_PROMPT = "You are a mortgage advisor advising mortgage brokers and you are  representing Precise Mortgages, a UK-based mortgage provider. As a representative for Precise Mortgages, your goal is to assist brokers in selecting the best mortgage products for their clients. You have access to the Precise Mortgages' criteria in the following file and you will only refer to this file:('/ocg.csv').if it says 'we may consider x' add that as a caveat instead of the main criteria. If brokers ask about a specific criteria point, you will provide them with the full criteria information related to that point.If you don't know the answer please refer to a live agent and do not fill the gaps with outside knowledge. This document is your only source of information.When the page has a title with a keyword please refer to that as the criteria for that keyword.."
DEFAULT_TITLE_GENERATION_USER_PROMPT = "You are a mortgage advisor advising mortgage brokers and you are  representing Precise Mortgages, a UK-based mortgage provider. As a representative for Precise Mortgages, your goal is to assist brokers in selecting the best mortgage products for their clients. You have access to the Precise Mortgages' criteria in the following file and you will only refer to this file:('/ocg.csv').if it says 'we may consider x' add that as a caveat instead of the main criteria. If brokers ask about a specific criteria point, you will provide them with the full criteria information related to that point.If you don't know the answer please refer to a live agent and do not fill the gaps with outside knowledge. This document is your only source of information.When the page has a title with a keyword please refer to that as the criteria for that keyword.."
=======
PROVIDER_PREFIX = "provider_"
PROVIDER_PRIVATE_CUSTOMIZATION_KEYS = [
    "tools",
    "tool_choice",
]

# Backend speciifc constants
API_BACKEND_DEFAULT_MODEL = "gpt-4o-mini"
>>>>>>> 2fed83cbae5504ac804d96aa11c51033d3f0028a

TITLE_GENERATION_MAX_CHARACTERS = 1500

OPEN_AI_MAX_TOKENS = 4096
OPEN_AI_MIN_SUBMISSION_TOKENS = 1
OPEN_AI_DEFAULT_MAX_SUBMISSION_TOKENS = 4000

# Config specific constants.
DEFAULT_PROFILE = 'default'
DEFAULT_CONFIG_DIR = 'llm-workflow-engine'
LEGACY_DEFAULT_CONFIG_DIR = 'chatgpt-wrapper'
DEFAULT_DATABASE_BASENAME = 'storage'
CONFIG_PROFILES_DIR = 'profiles'
DEFAULT_CONFIG = {
<<<<<<< HEAD
    'backend': 'api',
    'backend_options': {
        'default_user': None,
        'default_conversation_id': None,
    },
    'directories': {
        'templates': [
            '$CONFIG_DIR/profiles/$PROFILE/templates',
            '$CONFIG_DIR/templates',
        ],
        'presets': [
            '$CONFIG_DIR/presets',
            '$CONFIG_DIR/profiles/$PROFILE/presets',
        ],
        'plugins': [
            '$CONFIG_DIR/profiles/$PROFILE/plugins',
            '$CONFIG_DIR/plugins',
        ],
        'workflows': [
            '$CONFIG_DIR/workflows',
            '$CONFIG_DIR/profiles/$PROFILE/workflows',
        ],
        'functions': [
            '$CONFIG_DIR/functions',
            '$CONFIG_DIR/profiles/$PROFILE/functions',
        ],
    },
    'shell': {
        'prompt_prefix': '($TEMPERATURE/$MAX_SUBMISSION_TOKENS/$CURRENT_CONVERSATION_TOKENS): $SYSTEM_MESSAGE_ALIAS$NEWLINE$USER@$PRESET_OR_MODEL',
        'history_file': '%s%srepl_history.log' % (tempfile.gettempdir(), os.path.sep),
    },
    'database': None,
    'browser': {
        'provider': 'firefox',
        'debug': False,
        'plugins': [],
    },
    'model': {
        'default_preset': None,
        'default_system_message': 'default',
        'streaming': False,
        'system_message': {
            'programmer': SYSTEM_MESSAGE_ADVISOR,
            'creative_writer': SYSTEM_MESSAGE_CSB,
        },
    },
    'chat': {
        'log': {
            'enabled': False,
            'filepath': 'lwe.log',
=======
    "backend": "api",
    "backend_options": {
        "auto_create_first_user": None,
        "default_user": None,
        "default_conversation_id": None,
        "title_generation": {
            "provider": None,
            "model": None,
        },
    },
    "directories": {
        "cache": [
            "$DATA_DIR/cache",
        ],
        "templates": [
            "$CONFIG_DIR/profiles/$PROFILE/templates",
            "$CONFIG_DIR/templates",
        ],
        "presets": [
            "$CONFIG_DIR/presets",
            "$CONFIG_DIR/profiles/$PROFILE/presets",
        ],
        "plugins": [
            "$CONFIG_DIR/profiles/$PROFILE/plugins",
            "$CONFIG_DIR/plugins",
        ],
        "workflows": [
            "$CONFIG_DIR/workflows",
            "$CONFIG_DIR/profiles/$PROFILE/workflows",
        ],
        "tools": [
            "$CONFIG_DIR/tools",
            "$CONFIG_DIR/profiles/$PROFILE/tools",
        ],
    },
    "shell": {
        "prompt_prefix": "$TITLE$NEWLINE($TEMPERATURE/$MAX_SUBMISSION_TOKENS/$CURRENT_CONVERSATION_TOKENS): $SYSTEM_MESSAGE_ALIAS$NEWLINE$USER@$PRESET_OR_MODEL",
        "history_file": "%s%srepl_history.log" % (tempfile.gettempdir(), os.path.sep),
        "streaming": False,
    },
    "database": None,
    "model": {
        "default_preset": None,
        "default_system_message": "default",
        "system_message": {
            "programmer": SYSTEM_MESSAGE_PROGRAMMER,
            "creative_writer": SYSTEM_MESSAGE_CREATIVE_WRITER,
>>>>>>> 2fed83cbae5504ac804d96aa11c51033d3f0028a
        },
    },
    'log': {
        'console': {
            'level': 'error',
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    'plugins': {
        'enabled': [
            'echo',
        ],
    },
    'debug': {
        'log': {
            'enabled': False,
            'filepath': '%s%slwe-debug.log' % (tempfile.gettempdir(), os.path.sep),
            'level': 'debug',
            'format': '%(name)s - %(asctime)s - %(levelname)s - %(message)s',
        },
    },
}

# Shell specific constants.
COMMAND_LEADER = '/'
ACTIVE_ITEM_INDICATOR = "\U0001F7E2"  # Green circle.
LEGACY_COMMAND_LEADER = '!'
DEFAULT_COMMAND = 'ask'
DEFAULT_HISTORY_LIMIT = 20
SHELL_ONE_SHOT_COMMANDS = [
    'install',
    'reinstall',
    'config',
]

# Interface-specific constants.
NO_TITLE_TEXT = "No title"
# These are the variables in this file that are available for substitution in
# help messages.
HELP_TOKEN_VARIABLE_SUBSTITUTIONS = [
    'COMMAND_LEADER',
    'DEFAULT_HISTORY_LIMIT',
    'SYSTEM_MESSAGE_DEFAULT',
    'OPEN_AI_MAX_TOKENS',
    'OPEN_AI_MIN_SUBMISSION_TOKENS',
    'OPEN_AI_DEFAULT_MAX_SUBMISSION_TOKENS',
]