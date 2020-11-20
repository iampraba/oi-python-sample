from controllers.ClientSideException import ZOIException
from controllers.Operations import Delete, CreateDocument
from controllers.RestClient import ZOIRestClient

document_id = None

document_delete_url = None


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

        # Used for demonstration only
        from controllers.RestClient import ZOIConfigUtil
        for key in ZOIConfigUtil.config_prop_dict:
            print("{0}: {1}".format(key, ZOIConfigUtil.config_prop_dict[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def create_document():
    """
    Used to demonstrate working of Delete Document API
    """
    try:
        oi_demo_obj = CreateDocument.get_instance()

        response = oi_demo_obj.create_document()
        response_json = response.response_json

        global document_id, document_delete_url
        document_id = response_json["document_id"]
        document_delete_url = response_json["document_delete_url"]
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def sample_1():
    try:
        print("Created sample document...\ndocument_id: " + str(document_id) + "\ndocument_delete_url: " + str(
            document_delete_url), end="\n\n")

        oi_demo_obj = Delete.get_instance()

        oi_demo_obj.set_document_id(document_id)
        # oi_demo_obj.set_document_delete_url(document_delete_url)

        response = oi_demo_obj.delete_writer_document()
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
    print()
    create_document()
    print()
    sample_1()
