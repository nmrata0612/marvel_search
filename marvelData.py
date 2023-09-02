from marvel import Marvel

ID = Marvel("da3e2109f1b497980dc0180be6478265", "219d66e51b138f5a84f621cd06a0a1b278bac878")
character = ID.characters
all_character = character.all()['data']['results']


class MarvelData:

    @classmethod
    def hero_id(cls):
        id_list = []
        for char in all_character:
            id_list.append(char['id'])
        return id_list

    @classmethod
    def hero_name(cls):
        name_list = []
        for char in all_character:
            name_list.append(char['name'])
        return name_list

    @classmethod
    def search_hero_by_name(cls, name):
        search_character = character.all(nameStartsWith=name)['data']['results']
        search_result_list = []
        for char in search_character:
            search_result_list.append(char['name'])
        return search_result_list

    @classmethod
    def search_id_by_name(cls, name):
        search_character = character.all(nameStartsWith=name)['data']['results']
        search_result_list = []
        for char in search_character:
            search_result_list.append(char['id'])
        return search_result_list

    @classmethod
    def search_hero_thumbnail(cls, name):
        search_character = character.all(nameStartsWith=name)['data']['results']
        search_thumbanail_list = []
        for char in search_character:
            search_thumbanail_list.append(f"{char['thumbnail']['path']}.{char['thumbnail']['extension']}")
        return search_thumbanail_list

    @classmethod
    def hero_thumbnail(cls):
        thumbnail_list = []
        for char in all_character:
            thumbnail_list.append(f"{char['thumbnail']['path']}.{char['thumbnail']['extension']}")
        return thumbnail_list

    @classmethod
    def hero_description(cls):
        desc_list = []
        for char in all_character:
            desc_list.append(f"{char['description']}")
        return desc_list

    @classmethod
    def search_name_by_id(cls, char_id):
        character_id = int(char_id)
        all_char = character.get(character_id)['data']['results']
        return all_char[0]['name']

    @classmethod
    def search_description_by_id(cls, char_id):
        character_id = int(char_id)
        all_char = character.get(character_id)['data']['results']
        return all_char[0]['description']

    @classmethod
    def search_thumbnail_by_id(cls, char_id):
        character_id = int(char_id)
        all_char = character.get(character_id)['data']['results']
        return f"{all_char[0]['thumbnail']['path']}.{all_char[0]['thumbnail']['extension']}"

    @classmethod
    def search_comics_by_id(cls, char_id):
        character_id = int(char_id)
        all_char = character.get(character_id)['data']['results']
        all_comics = all_char[0]['comics']['items']
        comics = []
        for comic in all_comics:
            comics.append(comic['name'])
        return comics


data = MarvelData()
