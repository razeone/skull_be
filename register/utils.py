from register.models import Customer

ERROR_MESSAGES = {
    'user_not_found': {
        'error': 'The requested user was not found'
    },
    'activation_error': {
        'error': 'There was an error activating the user'
    }
}

SUCCESS_MESSAGES = {
    'user_activated': {
        'success': 'User was succesfully activated'
    }
}


def activate_user(id):
    try:
        customer = Customer.objects.get(id=id)

        if(customer is None):
            return ERROR_MESSAGES['user_not_found']
        else:
            try:
                customer.is_active = True
                customer.set_password(customer.password)
                customer.save()
                return SUCCESS_MESSAGES['user_activated']
            except ValueError:
                return ERROR_MESSAGES['activation_error']
    except ValueError:
        return ERROR_MESSAGES['activation_error']
