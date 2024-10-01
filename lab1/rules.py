from src.production import IF, AND, THEN, OR, DELETE, NOT, FAIL

TOURIST_RULES = (
    IF( #R1
        OR(
            '(?x) doesn\'t take pictures', 
            '(?x) is rude', 
            '(?x) wears a suit'
        ),
        THEN(
            '(?x) is self-important'
        )
    ),
    IF( #R2
        OR(
            '(?x) has a performant camera', 
            '(?x) wears designer clothes', 
            '(?x) visits top restaurants'
        ),
        THEN(
            '(?x) is rich'
        )
    ),
    IF( #R3
        OR(
            '(?x) speaks loudly', 
            '(?x) smokes in public', 
            '(?x) tackles others'
        ),
        THEN(
            '(?x) is inconsiderate'
        )
    ),
    IF( #R4
        AND(
            '(?x) is self-important',
            '(?x) is inconsiderate'
        ),
        THEN(
            '(?x) is a mouth-breather'
        )
    ),
    IF( #R5
        AND(
            '(?x) has a performant camera',
            '(?x) films a lot',
            '(?x) doesn\'t take pictures'
        ),
        THEN(
            '(?x) is a professional videographer'
        )
    ),
    IF( #R6
        AND(
            '(?x) is rich',
            '(?x) is a mouth-breather'
        ),
        THEN(
            '(?x) is an aristrocrat'
        )
    ),
    IF( #R7
        AND(
            '(?x) visits top restaurants',
            '(?x) has higher than average body mass'
        ),
        THEN(
            '(?x) is a gourmand'
        )
    ),
    IF( #R8
        AND(
            '(?x) is a professional videographer',
            '(?x) is a mouth-breather'
        ),
        THEN(
            '(?x) is a vlogger'
        )
    ),
    IF( #R9
        AND(
            '(?x) is inconsiderate',
            '(?x) has weird claims',
            '(?x) speaks Stellarian'
        ),
        THEN(
            '(?x) is an occupant'
        )
    ),
    IF( #R10
        AND(
            '(?x) speaks on the phone',
            '(?x) speaks a foreign language',
            '(?x) wears a suit'
        ),
        THEN(
            '(?x) is a business traveler'
        )
    )
)
