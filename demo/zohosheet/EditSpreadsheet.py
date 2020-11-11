import random

from controllers.ClientSideException import ZOIException
from controllers.Operations import EditSpreadsheet
from controllers.RestClient import ZOIRestClient


def configure():
    """
    Passing the entire configuration as a dictionary
    """
    try:
        config_obj = ZOIRestClient.get_instance()
        user_config = {
            "apikey": "2ae438cf864488657cc9754a27daa480",
            "writer_api_base_url": "https://api.office-integrator.com/writer/officeapi/",
            "sheet_api_base_url": "https://api.office-integrator.com/sheet/officeapi/",
            "show_api_base_url": "https://api.office-integrator.com/show/officeapi/"
        }
        config_obj.initialize(user_config)
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def edit_spreadsheet():
    try:
        document_id = random.randint(10000000, 100000000)  # Used for demonstration

        edit_sheet = EditSpreadsheet.get_instance()

        edit_sheet.set_user_info("display_name", "Matt")
        edit_sheet.set_document_info("document_id", document_id)
        edit_sheet.set_callback_settings("save_format", "xlsx")
        edit_sheet.set_callback_settings("save_url", "https://zylker.com/save.php")
        edit_sheet.set_callback_settings("context_info", "additional doc or user info")
        edit_sheet.upload_document("document", "../files/ZohoSheet.xlsx")

        response = edit_sheet.edit_spreadsheet()
        response_json = response.response_json
        for key in response_json:
            print("{0}: {1}".format(key, response_json[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


if __name__ == '__main__':
    configure()
    edit_spreadsheet()
