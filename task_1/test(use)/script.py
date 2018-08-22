import exrex as ex                            # pip install exrex
import task_1.develop.password_validator as pv
import task_1.develop.settings_information_and_methods as settings

#exrex позволяет генерировать строку по регулярному выражению
# create count passwords
def simple_test_password(count):
    if count > 150:
        raise Exception('Very big count!')
    pv.sett.clearing_a_file()
    for i in range(count):
        # creating a string by pattern
        token = ex.getone(settings.PATTERN,2)
        pv.password_validator_function(token)

