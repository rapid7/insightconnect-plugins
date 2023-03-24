class Cause:
    INVALID_DETAILS = "Invalid details provided."


class Assistance:
    VERIFY_INPUT = (
        "Verify your input is correct and not malformed and try again. If the issue persists, please contact support."
    )


accepted_empty_fields = ["cyberTerms", "cyberTermCves", "iocs"]
closing_ticket_reasons = {
    "Problem solved": "ProblemSolved",
    "Informational only": "InformationalOnly",
    "Problem we are already aware of": "ProblemWeAreAlreadyAwareOf",
    "Company owned domain": "CompanyOwnedDomain",
    "Legitimate application/profile": "LegitimateApplication/Profile",
    "Not related to my company": "NotRelatedToMyCompany",
    "False positive": "FalsePositive",
    "Other": "Other",
}
