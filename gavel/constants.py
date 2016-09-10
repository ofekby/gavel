ANNOTATOR_ID = 'annotator_id'

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
DEFAULT_WELCOME_MESSAGE = '''
Welcome to Gavel.

Gavel is a fully automated expo judging system that both tells you where to go
and collects your votes.

The system is based on the model of pairwise comparison. You'll start off by
looking at a single submission, and then for every submission after that,
you'll decide whether it's better or worse than the one you looked at
immediately beforehand.

If at any point, you can't find a particular submission, you can click the
'Skip' button and you will be assigned a new project. Please don't skip unless
absolutely necessary.

Gavel makes it really simple for you to submit votes, but please think hard
before you vote. Once you make a decision, you can't take it back.
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'Welcome to Gavel!'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Welcome to Gavel, the online expo judging system. This email contains your
magic link to the judging system.

DO NOT SHARE this email with others, as it contains your personal magic link.

To access the system, visit {link}.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()