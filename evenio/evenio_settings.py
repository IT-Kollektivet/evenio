from django.conf import settings

# Put settings and static stuff here!

DEFAULT_MONTH_SLUGS = {
    'januar': 1,
    'january': 1,
    'jan': 1,

    'februar': 2,
    'february': 2,
    'feb': 2,

    'marts': 3,
    'march': 3,
    'mar': 3,

    'april': 4,
    'apr': 4,

    'may': 5,
    'maj': 5,

    'juni': 6,
    'june': 6,
    'jun': 6,

    'juli': 7,
    'july': 7,
    'jul': 7,

    'august': 8,
    'aug': 8,

    'september': 9,
    'sep': 9,

    'oktober': 10,
    'october': 10,
    'oct': 10,
    'okt': 10,

    'november': 11,
    'nov': 11,
    
    'december': 12,
    'dec': 12,
}

MONTH_SLUGS = getattr(settings, "EVENIO_MONTH_SLUGS", DEFAULT_MONTH_SLUGS)

