from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'The password must contain a letter',
                code='password_no_letter'
            )

    def get_help_text(self):
        return 'Your password must contain at least one letter upper or lowercase.'

class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.is_digit() for char in password):
            raise ValidationError(
                'The password mus contain a number',
                code='password_no_number'
            )

    def get_help_text(self):
        return 'Your password must contain at least one number.'
