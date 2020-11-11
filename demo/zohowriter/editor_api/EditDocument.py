import random  # Imported to generate random document_id

from controllers.ClientSideException import ZOIException
from controllers.Operations import EditDocument
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


def edit_document():
    try:
        document_id = random.randint(10000000, 100000000)  # Used for demonstration

        edit_doc = EditDocument.get_instance()

        edit_doc.set_document_info("document_id", document_id)
        edit_doc.set_callback_settings("save_format", "docx")
        edit_doc.set_callback_settings("save_url", "https://domain.com/save.php")
        edit_doc.set_user_info("user_id", "2000")
        edit_doc.set_user_info("display_name", "Anil")
        edit_doc.upload_document("document", "../../../files/ZohoWriter.docx")
        # edit_doc.set_url("File URL Here")

        response = edit_doc.edit_document()
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
    edit_document()
