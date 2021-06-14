class PatientHospitalMismatch(Exception):
  """ Raised when the patient found does not belong to the appropriate hospital """


class MissingHospitalName(Exception):
  """ Raised when hospital payload is missing a name """
