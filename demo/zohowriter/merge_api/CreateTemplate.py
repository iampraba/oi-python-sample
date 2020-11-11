from controllers.ClientSideException import ZOIException
from controllers.Operations import CreateTemplate
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


def create_template():  # TODO Add setters for 'merge_data_csv_url' and 'merge_data_json_url'
    try:
        create_template = CreateTemplate.get_instance()

        create_template.set_callback_settings("save_format", "docx")
        create_template.set_callback_settings("save_url", "https://domain.com/save.php")
        create_template.upload_document("merge_data_json_content", "../../../files/mergedata.json")

        response = create_template.create_template()
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
    create_template()
