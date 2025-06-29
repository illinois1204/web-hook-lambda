import enum


class StageCode(enum.StrEnum):
    TODO = "10000"
    IN_PROGRESS = "3"
    IN_REVIEW = "10100"
    QA = "10101"
    DONE = "10001"


class TransitCode(enum.StrEnum):
    TODO = "11"
    IN_PROGRESS = "21"
    IN_REVIEW = "41"
    QA = "51"
    DONE = "31"
