class Levels:
    KG = "kindergarden"
    PR = "primary"
    SE = "secondary"
    HS = "high_school"

    @classmethod
    def choices(cls):
        return (
            (cls.KG, "Kindergarden"),
            (cls.PR, "Primary"),
            (cls.SE, "Secondary"),
            (cls.HS, "High School"),
        )


class Schools:
    LA = "language_and_arts"
    SC = "sciences_technology_and_math"
    SS = "social_sciencies_and_humanities"
    PE = "sports"

    @classmethod
    def choices(cls):
        return (
            (cls.LA, "Language and Arts"),
            (cls.SC, "Sciences Technology and Math"),
            (cls.SS, "Social Sciences and Humanities"),
            (cls.PE, "Sports"),
        )
