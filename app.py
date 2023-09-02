from flask import Flask, render_template, request
from marvelData import MarvelData

app = Flask(__name__)
app.secret_key = 'Namrat0612'


@app.route('/')
def home():
    all_names = MarvelData.hero_name()
    thumbnail = MarvelData.hero_thumbnail()
    all_id = MarvelData.hero_id()
    list1 = zip(all_id, all_names, thumbnail)
    return render_template('index.jinja2', heroes=list1)


@app.route('/search_result', methods=['GET', 'POST'])
def search_result():
    search_name = (request.form['search_name'])
    if search_name == "":
        return render_template('errorPage.jinja2', message=f"so result found ")
    search_data = MarvelData.search_hero_by_name(search_name)
    if not search_data:
        return render_template('errorPage.jinja2', message=f"so result found ")
    search_thumbnail = MarvelData.search_hero_thumbnail(search_name)
    search_id = MarvelData.search_id_by_name(search_name)
    list2 = zip(search_id, search_data, search_thumbnail)
    return render_template('searchResult.jinja2', search_result=list2)


@app.route('/<string:post_id>')
def post_for_page(post_id):
    name = MarvelData.search_name_by_id(post_id)
    description = MarvelData.search_description_by_id(post_id)
    thumbnail = MarvelData.search_thumbnail_by_id(post_id)
    comic_list = MarvelData.search_comics_by_id(post_id)
    return render_template('posts.jinja2', post_id=post_id, name=name, description=description, thumbnail=thumbnail,
                           comic_list=comic_list)


if __name__ == '__main__':
    app.run(debug=True)
