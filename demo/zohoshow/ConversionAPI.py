from controllers.APIHelper import APIResponse, FileAPIResponse
from controllers.ClientSideException import ZOIException
from controllers.Operations import ConvertPresentation
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


def convert_presentation():
    try:
        convert_show = ConvertPresentation.get_instance()

        convert_show.upload_document("document", "../files/ZohoShow.pptx")
        convert_show.set_format("pdf")

        response = convert_show.convert_presentation()
        if isinstance(response, APIResponse):
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        elif isinstance(response, FileAPIResponse):
            output_file_name = "conversion_" + response.file_name
            output_file_name = output_file_name.replace("\"", "")
            with open(output_file_name, "wb") as f:
                f.write(response.file_content)
            print("Converted document stored in output folder with filename : " + output_file_name)
        else:
            print(str(response))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


if __name__ == '__main__':
    configure()
    convert_presentation()
