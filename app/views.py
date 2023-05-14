from flask import render_template, redirect, url_for

from . import app, db
from .models import Films, Reviews
from .forms import ReviewForm, MovieForm


@app.route('/')
def index_page():
    films = Films.query.order_by(Films.id).all()
    return render_template('index.html', films=films)


@app.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
def movie_page(movie_id):
    movie = Films.query.get(movie_id)
    form = ReviewForm()
    if movie.reviews:
        avg_score = round((sum(review.score for review in movie.reviews) / len(movie.reviews)), 1)
    else:
        avg_score = 0
    if form.validate_on_submit():
        review = Reviews()
        review.author = form.author.data
        review.text = form.text.data
        review.score = form.score.data
        review.film_id = movie_id
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('movie_page', movie_id=movie_id))
    return render_template('movie.html', movie=movie, avg_score=avg_score, form=form)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie_page():
    form = MovieForm()
    if form.validate_on_submit():
        movie = Films()
        movie.title = form.title.data
        movie.text = form.text.data
        image = form.image.data
        image_name = secure_filename(image.filename)
        UPLOAD_FOLDER.mkdir(exist_ok=True)
        image.save(UPLOAD_FOLDER / image_name)
        movie.path = image_name
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('movie_page', movie_id=movie.id))
    return render_template('add_movie.html', form=form)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews_page():
    reviews = Reviews.query.order_by(Reviews.created_date.desc()).all()
    movies = Films.query.all()
    return render_template('reviews.html', reviews=reviews, movies=movies)


@app.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    review = Reviews.query.get(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('reviews_page'))
