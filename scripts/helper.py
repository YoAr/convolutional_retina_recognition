
import configparser

class HelperFacade:
    @staticmethod
    def get_data_file_path():
        """Reads the config file and returns the path to the data file."""
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['DATASOURCE']['file_path']
