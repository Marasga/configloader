import json
from typing import Union

class ConfigLoader():
    """
        Simply load a json config (single level) and expose some methods to help handling it
    
        :param uri: str, dict Path of the config json file | config dictionary

    """
    instance_count = 0    

    def __init__(self,uri:Union[str, dict] ) -> None:
        '''
            Constructor, can create config from file or dictionary
        '''
        if type(uri)==str: 
            with open(uri, mode='r', encoding='utf-8') as f:
                self.CONFIG = json.load(f)
        elif type(uri)==dict:
            self.CONFIG=uri
        else:
            # TODO: Create custom exception
            raise Exception('Invalid type, accept string (path of json) or dict')
        
    
    def get_property(self,property_name: str) -> any:
        '''
            Return property value for specifed key
        '''
        if property_name in self.CONFIG:
            prop = self.CONFIG[property_name]
        else :
            raise KeyError('Missing requested config property')
        return prop

    def set_property(self,key: str,value: any) -> any:
        '''
            Set property value for specifed key
        '''
        self.CONFIG[key] = value
        return value

    def list_properties(self) -> list:
        '''
            List all available properties in config
        '''
        properties = list(self.CONFIG.keys())
        print(properties)
        return properties

    def overwrite(self, config: dict) -> None:
        '''
            Overwrite existing instance config value with given dictionary
        '''
        self.CONFIG = config
        return None
    
    def import_config(self,uri:str) -> None:
        '''
            Import and overwrite existing config loading config from file
        '''
        with open(uri, mode='r', encoding='utf-8') as f:
            self.CONFIG = json.load(f)
    
    def export_config(self, uri:str) -> None:
        '''
            Export current config to file
        '''
        with open(uri, mode='w', encoding='utf-8') as f:
            self.CONFIG = json.dump(f)


def main():
    config = ConfigLoader('json_data.json')
    config.list_properties()

    diz = {'prop1':2,'prop2':["a",1]}
    config2 = ConfigLoader(diz)
    config2.list_properties()

if __name__ == "__main__":
    main()
else:
    print ("Executed when imported")
