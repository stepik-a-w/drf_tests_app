from split_settings.tools import include, optional

include(
    'base/env.py', optional('local/env.py'),
    'base/root.py',
    'base/common.py',
    'base/logging.py', optional('local/logging.py'),
    'base/security.py', optional('local/security.py'),
    'base/middleware.py',
    'base/apps.py',
    'base/*.py',

    optional('local/*.py'),
)
