from utilities import NumericValidator


def _validate_field(field_edit):
    field_edit.setValidator(NumericValidator())
