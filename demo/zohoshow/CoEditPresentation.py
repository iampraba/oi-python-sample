import random

from controllers.ClientSideException import ZOIException
from controllers.Operations import CoEditPresentation
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


def co_edit_presentation():
    try:
        document_id = random.randint(10000000, 100000000)  # Used for demonstration

        co_edit_show = CoEditPresentation.get_instance()

        co_edit_show.set_user_info("user_id", "3000")
        co_edit_show.set_user_info("display_name", "Anil")
        co_edit_show.set_callback_settings("save_format", "pptx")
        co_edit_show.set_document_info("document_id", document_id)
        co_edit_show.set_callback_settings("save_url", "https://domain.com/save.php")
        co_edit_show.set_callback_settings("context_info", "additional doc or user info")
        co_edit_show.upload_document("document", "../files/ZohoShow.pptx")

        response = co_edit_show.co_edit_presentation()
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
    co_edit_presentation()
