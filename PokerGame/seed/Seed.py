import json
import random
import sys


class Seed:
    STORAGE_FILE: str = 'seed/seed.json'

    def __init__(self, seed_name: str = None):
        self.seed: int = self.__generate() if seed_name is None else self.__load(seed_name)

    def __repr__(self):
        return 'represent the seed used for current game'

    def __load(self, seed_name: str) -> int:
        """
        load the given seed from the json file
        :return bool:
        """
        try:
            with open(self.STORAGE_FILE, 'r') as f:
                file_content: list = json.load(f)
                f.close()

            for name in file_content:
                if name == seed_name:
                    seed = file_content[name]
                    random.seed(seed)
                    random.random()
                    return seed
        except FileNotFoundError:
            print('File Not found')

    def __generate(self) -> int:
        """
        generate new seed
        :return:
        """
        seed = random.randrange(sys.maxsize)
        random.seed(seed)
        random.random()

        return seed

    def save(self, seed_name: str) -> bool:
        """
        save the seed in the json file specified
        :return bool:
        """
        seed_name = seed_name.replace(' ', '_')
        try:
            # get values from the file
            with open(self.STORAGE_FILE, 'r') as f:
                file_content: dict = json.load(f)
                f.close()

            if seed_name in file_content.keys():
                return False
            file_content[seed_name] = self.seed

            # override current file with new values
            with open(self.STORAGE_FILE, 'w') as f:
                json.dump(file_content, f)
                f.close()

            return True
        except FileNotFoundError:
            print('File not found')
