from controllers.ClientSideException import ZOIException
from controllers.Operations import CompareDocuments
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


def compare_document():
    try:
        compare_document = CompareDocuments.get_instance()

        compare_document.upload_document("document1", "../files/CompareDocument1.docx")
        # compare_document.set_url1("File URL Here")
        compare_document.upload_document("document2", "../files/CompareDocument2.docx")
        # compare_document.set_url2("File URL Here")
        compare_document.set_title("Doc1_and_Doc2")
        # compare_document.set_lang("en")

        response = compare_document.compare_documents()
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
    compare_document()
