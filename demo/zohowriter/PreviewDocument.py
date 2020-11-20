from controllers.ClientSideException import ZOIException
from controllers.Operations import PreviewDocument
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


def sample_1():
    try:
        oi_demo_obj = PreviewDocument.get_instance()

        oi_demo_obj.set_lang("en")
        oi_demo_obj.set_url("https://file-examples-com.github.io/uploads/2017/02/file-sample_500kB.docx")

        response = oi_demo_obj.preview_document()
        response_json = response.response_json
        for key in response_json:
            print("{0}: {1}".format(key, response_json[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def sample_2():
    try:
        oi_demo_obj = PreviewDocument.get_instance()

        oi_demo_obj.set_lang("en")
        oi_demo_obj.upload_document("document", "../files/ZohoWriter.docx")

        response = oi_demo_obj.preview_document()
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
    sample_1()
    print()
    sample_2()
