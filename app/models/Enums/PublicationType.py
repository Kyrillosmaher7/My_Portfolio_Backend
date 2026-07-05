
import enum


class PublicationType(str, enum.Enum):
    '''
      Enum for publication types.
    '''
    CONFERENCE_PAPER = "Conference Paper"
    WORKSHOP_PAPER = "Workshop Paper"
    PREPRINT = "Preprint"
    THESIS = "Thesis"
    JOURNAL_ARTICLE = "Journal Article"