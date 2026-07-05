import enum


class PublicationStatus(str, enum.Enum):
    """Enum for publication status of a publication."""
    PUBLISHED = "Published"
    UNDER_REVIEW = "Under Review"
    DRAFT = "Draft"