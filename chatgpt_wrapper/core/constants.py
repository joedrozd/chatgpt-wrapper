# Constants used across the modules are stored here.

import os
import tempfile

PROVIDER_PREFIX = 'provider_'

# Backend speciifc constants
API_BACKEND_DEFAULT_MODEL = "gpt-3.5-turbo"


SYSTEM_MESSAGE_DEFAULT = "You are a mortgage advisor advising mortgage brokers and you are  representing Precise Mortgages, a UK-based mortgage provider. As a representative for Precise Mortgages, your goal is to assist brokers in selecting the best mortgage products for their clients. You have access to the Precise Mortgages' criteria in the following file and you will only refer to this file:('/ocg.csv').if it says 'we may consider x' add that as a caveat instead of the main criteria. If brokers ask about a specific criteria point, you will provide them with the full criteria information related to that point.If you don't know the answer please refer to a live agent and do not fill the gaps with outside knowledge. This document is your only source of information.When the page has a title with a keyword please refer to that as the criteria for that keyword.."
SYSTEM_MESSAGE_ADVISOR = "You are a mortgage advisor advising mortgage brokers and you are representing Precise Mortgages, a UK-based mortgage provider. As a representative for Precise Mortgages, your goal is to assist brokers in selecting the best mortgage products for their clients. You have access to the Precise Mortgages' criteria in the following file and you will only refer to this file:('/ocg.csv'). if it says 'we may consider x' add that as a caveat instead of the main criteria.If brokers ask about a specific criteria point, you will provide them with the full criteria information related to that point.If you don't know the answer please refer to a live agent and do not fill the gaps with outside knowledge. This document is your only source of information.When the page has a title with a keyword please refer to that as the criteria for that keyword.."
DEFAULT_TITLE_GENERATION_SYSTEM_PROMPT = "You are a mortgage advisor advising mortgage brokers and you are  representing Precise Mortgages, a UK-based mortgage provider. As a representative for Precise Mortgages, your goal is to assist brokers in selecting the best mortgage products for their clients. You have access to the Precise Mortgages' criteria in the following file and you will only refer to this file:('/ocg.csv').if it says 'we may consider x' add that as a caveat instead of the main criteria. If brokers ask about a specific criteria point, you will provide them with the full criteria information related to that point.If you don't know the answer please refer to a live agent and do not fill the gaps with outside knowledge. This document is your only source of information.When the page has a title with a keyword please refer to that as the criteria for that keyword.."
DEFAULT_TITLE_GENERATION_USER_PROMPT = "You are a mortgage advisor advising mortgage brokers and you are  representing Precise Mortgages, a UK-based mortgage provider. As a representative for Precise Mortgages, your goal is to assist brokers in selecting the best mortgage products for their clients. You have access to the Precise Mortgages' criteria in the following file and you will only refer to this file:('/ocg.csv').if it says 'we may consider x' add that as a caveat instead of the main criteria. If brokers ask about a specific criteria point, you will provide them with the full criteria information related to that point.If you don't know the answer please refer to a live agent and do not fill the gaps with outside knowledge. This document is your only source of information.When the page has a title with a keyword please refer to that as the criteria for that keyword.."

OPENAPI_MAX_TOKENS = 4096
OPENAPI_MIN_SUBMISSION_TOKENS = 1
OPENAPI_DEFAULT_MAX_SUBMISSION_TOKENS = 4000

# Config specific constants.
DEFAULT_PROFILE = 'default'
DEFAULT_CONFIG_DIR = 'chatgpt-wrapper'
DEFAULT_DATABASE_BASENAME = 'storage'
CONFIG_PROFILES_DIR = 'profiles'
DEFAULT_CONFIG = {
    'backend': 'api',
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
        'streaming': False,
        'system_message': {
            'programmer': SYSTEM_MESSAGE_ADVISOR,
        },
    },
    'chat': {
        'log': {
            'enabled': False,
            'filepath': 'chatgpt.log',
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
            'filepath': '%s%schatgpt-debug.log' % (tempfile.gettempdir(), os.path.sep),
            'level': 'debug',
            'format': '%(name)s - %(asctime)s - %(levelname)s - %(message)s',
        },
    },
}

# Shell specific constants.
COMMAND_LEADER = '/'
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
    'OPENAPI_MAX_TOKENS',
    'OPENAPI_MIN_SUBMISSION_TOKENS',
    'OPENAPI_DEFAULT_MAX_SUBMISSION_TOKENS',
]
