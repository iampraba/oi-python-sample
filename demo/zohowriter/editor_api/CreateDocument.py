import random

from controllers.ClientSideException import ZOIException
from controllers.Operations import CreateDocument
from controllers.RestClient import ZOIRestClient


def configure():
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


def create_document():

    # ALTERNATE WAYS TO PASS ON THE CONFIGURATION - SAME APPLIES FOR ALL METHODS IN THIS SDK

    # create_doc.set_bulk_callback_settings(save_format_or_list="docx", save_url="https://domain.com/save.php")
    # create_doc.set_bulk_callback_settings("docx", save_url="https://domain.com/save.php")
    # create_doc.set_bulk_callback_settings(save_url="https://domain.com/save.php")

    # my_callback_settings = [
    #     "save_format": "docx",
    #     "save_url": "https://domain.com/save.php",
    # ]
    # create_doc.set_bulk_callback_settings(my_callback_settings)

    try:
        document_id = random.randint(10000000, 100000000)  # Used for demonstration

        create_doc = CreateDocument.get_instance()

        create_doc.set_document_info("document_id", document_id)
        create_doc.set_callback_settings("save_format", "docx")
        create_doc.set_callback_settings("save_url", "https://domain.com/save.php")

        response = create_doc.create_document()
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
    create_document()
