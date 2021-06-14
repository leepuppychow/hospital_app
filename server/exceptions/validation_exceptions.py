class PatientHospitalMismatch(Exception):
  """ Raised when the patient found does not belong to the appropriate hospital """


class MissingHospitalName(Exception):
  """ Raised when hospital payload is missing a name """


class MissingPatientData(Exception):
  """ Raised when patient payload is missing a first or last name """
