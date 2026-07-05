import enum


class SkillCategory(str, enum.Enum):
    """Enum for skill categories."""
    RESEARCH = "research"
    ML_FRAMEWORKS = "ml_frameworks"
    LANGUAGES_TOOLS = "languages_tools"
    DATA_INFRA = "data_infra"
    SOFT = "soft"