from controllers.ClientSideException import ZOIException
from controllers.Operations import Delete, CreateSpreadsheet
from controllers.RestClient import ZOIRestClient

session_id = None

session_delete_url = None


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


def create_spreadsheet():
    """
    Used to demonstrate working of Delete Spreadsheet API
    """
    try:

        oi_demo_obj = CreateSpreadsheet.get_instance()

        response = oi_demo_obj.create_spreadsheet()
        response_json = response.response_json

        global session_id, session_delete_url
        session_id = response_json["session_id"]
        session_delete_url = response_json["session_delete_url"]
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def sample_1():
    try:
        print("Created sample sheet...\nsession_id: " + str(session_id) + "\nsession_delete_url: " + str(
            session_delete_url), end="\n\n")

        oi_demo_obj = Delete.get_instance()

        oi_demo_obj.set_session_id(session_id)
        # oi_demo_obj.set_session_delete_url(session_delete_url)

        response = oi_demo_obj.delete_sheet_session()
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
    create_spreadsheet()
    print()
    sample_1()
