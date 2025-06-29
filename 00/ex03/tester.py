from NULL_not_found import NULL_not_found

Garlic = float("NaN")
Nothing = None
Fake = False
Empty = ''
Zero = 0

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)

print(NULL_not_found("Brian"))
